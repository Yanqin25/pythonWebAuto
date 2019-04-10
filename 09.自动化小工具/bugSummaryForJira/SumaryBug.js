let http = require('superagent')
let cheerio = require('cheerio')


let url = 'http://jira.300.cn/browse/'
let jsessionidFull = ''
//排除指定类型的bug,多个逻辑或
function excludeBug(bugData, excludes) {
    for (var i = bugData.length - 1; i >= 0; i--) {
        excludes.some(function(filter) {
            if (bugData[i].bugDesc.search(filter) != -1) {
                bugData.splice(i, 1);
                return true
            }
        })

    }
    return bugData
}

//留下指定类型的bug，多个逻辑或
function includeBug(bugData, includes) {
    let list = []
    bugData.forEach(function(item) {
        includes.forEach(function(filter) {
            if (item.bugDesc.search(filter) != -1) {
                list.push(item)
            }
        })
    })
    return list
}

//统计bug
function countBug(bugData) {
    var promise = new Promise(function(resolve, reject) {
        let bugCount = bugData.length;
        let major = 0; //一般
        let critical = 0; //严重
        let minor = 0; //建议
        let blocker = 0; //危险
        let revised = 0; //已修复
        let solving = 0; //解决问题中
        let left = 0; //遗留
        let discard = 0; //废弃
        let toVerfy = 0; //验证
        let newRequire = 0; //创建需求
        if (bugCount === 0) {
            reject('你还未登录，请重新手工登录并更新JSESSIONID');
            return;
        }
        bugData.forEach(function(item) {
            let status = item.bugStatus
            let priority = item.bugPriority
            switch (priority) {
                case '一般':
                    major++;
                    break;
                case '严重':
                    critical++;
                    break;
                case '建议':
                    minor++;
                    break;
                case '危险':
                    blocker++;
                    break;
                default:
                    reject("该优先级未定义：" + major);
                    return
            }
            switch (status) {
                case '已修复':
                    revised++;
                    break;
                case '解决问题中':
                    solving++;
                    break;
                case '遗留':
                    left++;
                    break;
                case '废弃':
                    discard++
                    break;
                case '验证':
                    toVerfy++;
                    break;
                case '创建需求':
                    newRequire++;
                    break;
                default:
                    reject("该状态未定义：" + status);
                    return
            }
        })

        var sumaryRuslt = {
            totalBug: bugCount,
            totalBlocker: blocker,
            totalCritical: critical,
            totalMajor: major,
            totalMinor: minor,
            closeTotal: revised + discard,
            closeRevised: revised,
            closeDiscard: discard,
            openTotal: solving + left + toVerfy + newRequire,
            openSolving: solving,
            openLeft: left,
            openToverfy: toVerfy,
            newRequire: newRequire
        }
        var reslut = {
            sumaryRuslt: sumaryRuslt,
            bugDetail: bugData
        }
        resolve(reslut)

    })

    return promise


}
//解析HTML
function resolveHtml(html) {
    var promise = new Promise(function(resolve, reject) {
        let $ = cheerio.load(html)
        let bugs = $('.links-list').find('dd')
        let bugData = []
        let promiseArray = []
        bugs.each(function(item) {
            let bug = $(this)
            let bugId = bug.find('p').children('span').attr('title').split(':')[0]
            let bugDesc = bug.find('p').children('span').attr('title').split(':')[1]
            let bugPriority = bug.find('.priority img').attr('src').split('/')[4].split('.')[0]
            let bugStatus = bug.find('.status span').text()
            let bugLink = 'http://jira.300.cn' + bug.find('a').attr('href')
            switch (bugPriority) {
                case 'major':
                    bugPriority = '一般';
                    break;
                case 'critical':
                    bugPriority = '严重';
                    break;
                case 'minor':
                    bugPriority = '建议';
                    break;
                case 'blocker':
                    bugPriority = '危险';
                    break;
                default:
                    reject("解析时该优先级未定义：" + major);
                    return
            }
            let bugItem = {
                bugId: bugId,
                bugDesc: bugDesc,
                bugPriority: bugPriority,
                bugStatus: bugStatus,
                bugLink: bugLink
                // bugOwner: bugOwner
            }
            promiseArray.push(findBugDetail(bugLink).then(bugDetail => {
                bugItem.bugTime = bugDetail.bugTime
                bugItem.bugReporter = bugDetail.bugReporter
                bugItem.bugOwner = bugDetail.bugOwner
                bugItem.bugCharge = bugDetail.bugCharge
                bugData.push(bugItem)
            }))
        })
        //耗时较长
        Promise.all(promiseArray).then(function() {
            resolve(bugData)
        })
    })

    return promise

}

//  解析bugDetail,包含bug的时间，经办人，报告人，处理人
//每个bug都去解析时间，经办人等，耗时较长
function resolveBugDetail(html) {
    let $ = cheerio.load(html)
    let bugTime = $('#create-date time').attr('datetime').replace(/T|\+.*/g, ' ')
    let bugReporter = $('#reporter-val .user-hover').text().trim()
    let bugOwner = $('span[data-name=BUG处理人] .user-hover').text().trim()
    let bugCharge = $('#assignee-val .user-hover').text().trim()
    let bugDetail = {
        bugTime: bugTime, //创建时间
        bugReporter: bugReporter, //报告人
        bugOwner: bugOwner, //bug处理人
        bugCharge: bugCharge
    }
    return bugDetail
}

function findBugDetail(bugLink) {
    var promise = new Promise(function(resolve, reject) {
        url = bugLink
        http.get(url).set({
            'Cookie': 'JSESSIONID=' + jsessionidFull
        }).then(res => {
            let bugDetail = resolveBugDetail(res.text);
            resolve(bugDetail)
        }).catch(err => {
            reject(err)
        })
    })
    return promise;
}

function postRequest(jsessionid, requireNo, modle, filterMap) {
    var promise = new Promise(function(resolve, reject) {
        url = 'http://jira.300.cn/browse/' + requireNo
        jsessionidFull = jsessionid
        http.get(url)
            .set({
                'Cookie': 'JSESSIONID=' + jsessionid
            })
            .then(res => {
                resolveHtml(res.text).then(function(bugData) {
                    if (modle === 'include' && filterMap.trim().length != 0) {
                        let includes = filterMap.split(';')
                        bugData = includeBug(bugData, includes)
                    }
                    if (modle === 'exclude' && filterMap.trim().length != 0) {
                        let excludes = filterMap.split(';')
                        bugData = excludeBug(bugData, excludes)
                    }
                    resolve(bugData)
                })
            })
            .catch(err => {
                reject(err)
            })
    })

    return promise


}

module.exports.countBug = countBug;
// module.exports.findBugDetail = findBugDetail;
module.exports.postRequest = postRequest;