#!/usr/bin/python3.7

from common import is_upper_case, \
                   sort_textbooks, \
                   shortenToDate

# test is in uppercase
message = 'ACSKLDFJSgSKLDFJSKLDFJ'
print('message {} in uppercase? {}'.format(message, is_upper_case(message)))

# sort strings in list
textbooks = ['z', 'Z', 'c', 'A', 'a']
print('sorting, before: {} after: {}'.format(textbooks, sort_textbooks(textbooks)))

# shortenToDate
message = 'Friday May 2, 7pm'
print('shorten, before: {} after: {}'.format(message, shortenToDate(message)))
