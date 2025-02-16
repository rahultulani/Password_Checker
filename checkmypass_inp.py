# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:34:18 2020

@author: rahul
"""     

import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code},check the api and try again')
    return res

def read_res(response):
    print(response.text)

def get_password_leaks_count(hashes,hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    #print(hashes)
    for h,count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    #check password if it exists in API response
    #print(password.encode('utf-8'))
    #print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    #print(first5_char, tail)
    #print(response)
    return get_password_leaks_count(response, tail)

def main(args):
        count = pwned_api_check(args)
        if count:
            print(f'{args} was found {count} times..you should change your password')
        else:
            print(f'{args} was not found..carry on')
        return 'done!'

def get_inp():
    print('Enter your password. Do not worry, we do not see what you enter')
    (main(input()))

if __name__ == '__main__':
    count = 1
    get_inp()
    while count:
        print('Do you want to check any other password? Y or N')
        inp = input()
        if inp == 'Y' or inp == 'y':
            get_inp()
        else:
            if inp == 'N' or inp == 'n':
                print('Bbye, take care')
                break
            else:
                print('please enter correct input..Either Y or N')
                continue