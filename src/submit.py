from time import localtime
import mechanize


class User:
    def __init__(self, f_name, l_name, email, address, city, state, zipcode, phone, gender, cable):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phone = phone
        self.gender = gender
        self.cable = cable

def mech_hgtv(url, form, user):
    """ mechanize hgtv dream home form 
    """
    br = mechanize.Browser()
    br.open(url)
    br.select_form(name = form)
    br['fvFirstName'] = user.f_name
    br['fvLastName'] = user.l_name 
    br['fvEmail'] = user.email
    br['fvConfirmEmail'] = user.email
    br['fvAddress1'] = user.address
    br['fvCity'] = user.city
    br.form.set_value([user.state],name='fvState')
    br['fvZip'] = user.zipcode
    # xxx xxx-xxxx format
    br['fvPhone'] = user.phone
    # 'm' or 'f'
    br.form.set_value([user.gender],name='fvGender')
    br.form.set_value([user.cable],name='fvOptIn33')
    br.submit()
    output =  br.response().read()
    yield output

def time_stamp():
    """local time stamp eg. YYYY:MM:DD:HH:MM"""
    stamp = localtime()
    year, month, day, hour, minute  = stamp[0:5]
    time_stamp_format = "{0}:{1}:{2}:{3}:{4}"\
            .format(year, month, day, hour, minute)
    return time_stamp_format

if __name__ == '__main__':

    sites = ["https://www.hgtv.com/design/hgtv-dream-home/sweepstakes"]
    u1 = User('Garrett', 'Johnson', 'garrett@hightenfund.com', '629 Effie Way', 'Raleigh', 'North Carolina', '27603', '248 346-7156', 'm', 'Spectrum')
    u2 = User('Elizabeth', 'Hammel', 'ebhammel@outlook.com', '629 Effie Way', 'Raleigh', 'North Carolina', '27603', '980 330-3120', 'f', 'Spectrum')
    u3 = User('Elizabeth', 'Hammel', 'ebhammel@outlook.com', '629 Effie Way', 'Raleigh', 'North Carolina', '27603', '980 330-3120', 'f', 'Spectrum')
    users = [u1]
    for site in sites:
        for user in users:
            mech_hgtv(site, 'sweepsEntryForm', user)

    submit_time = time_stamp()

    with open('log.txt', mode="a") as log:
        log.write(submit_time)