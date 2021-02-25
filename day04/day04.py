import re


def get_input(filename):

    with open(filename) as f:
        passports = f.read().split('\n\n')

    return passports


def valid_passports(passports):

    passport_dict = {}

    for i, passport in enumerate(passports):

        new_entry = dict(item.split(":") for item in re.split(" |\n", passport))
        if len(new_entry) == 7:
            if 'cid' not in new_entry.keys():
                passport_dict.update({i: new_entry})
        elif len(new_entry) == 8:
            passport_dict.update({i: new_entry})

    return passport_dict


def check_byr(passport):
    return 1920 <= int(passport['byr']) <= 2002


def check_iyr(passport):
    return 2010 <= int(passport['iyr']) <= 2020


def check_eyr(passport):
    return 2020 <= int(passport['eyr']) <= 2030


def check_hgt(passport):

    if passport['hgt'][-2:] == 'cm':
        return 150 <= int(passport['hgt'].split('c')[0]) <= 193
    elif passport['hgt'][-2:] == 'in':
        return 59 <= int(passport['hgt'].split('i')[0]) <= 76

    return False


def check_hcl(passport):

    pattern = '^#[(0-9)|(a-z)]{6}$'
    result = re.search(pattern, passport['hcl'])

    return result is not None


def check_ecl(passport):
    eye_colours = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    return passport['ecl'] in eye_colours


def check_pid(passport):

    pattern = '^[0-9]{9}$'
    result = re.search(pattern, passport['pid'])

    return result is not None


def requirements(passport_dict):

    byr_checked = dict(filter(lambda x: check_byr(x[1]), passport_dict.items()))
    iyr_checked = dict(filter(lambda x: check_iyr(x[1]), byr_checked.items()))
    eyr_checked = dict(filter(lambda x: check_eyr(x[1]), iyr_checked.items()))
    hgt_checked = dict(filter(lambda x: check_hgt(x[1]), eyr_checked.items()))
    hcl_checked = dict(filter(lambda x: check_hcl(x[1]), hgt_checked.items()))
    ecl_checked = dict(filter(lambda x: check_ecl(x[1]), hcl_checked.items()))
    all_checked = dict(filter(lambda x: check_pid(x[1]), ecl_checked.items()))

    return len(all_checked)


def main():
    passport_list = get_input('day04.txt')
    passport_dict = valid_passports(passport_list)
    all_checked = requirements(passport_dict)
    print(all_checked)


if __name__ == '__main__':
    main()
