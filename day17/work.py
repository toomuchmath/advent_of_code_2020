import pandas as pd

df = pd.DataFrame(columns=['Email.CreatedById',
                           'Email.CreatedDate',
                           'Email.Email_Id__c',
                           'Email.HasAttachment',
                           'Email.Id',
                           'Email.Incoming',
                           'Email.LastModifiedById',
                           'Email.LastModifiedDate',
                           'Email.MessageDate',
                           'Email.RelatedToId',
                           'Email.Status',
                           'Email.ToAddress',
                           'Email.ValidatedFromAddress',
                           'Case.RecordTypeId',
                           'Case_Owner__c',
                           'Status',
                           'Country__c',
                           'cLanguage__c',
                           'Case.Reason',
                           'Case.Sub_Type__c',
                           'Case.Legal_Entity__c',
                           'Case.CaseNumber',
                           'Case.Id',
                           'Case.CreatedById',
                           'Case.CreatedDate',
                           'Case.ContactId',
                           'Account_Brand__c',
                           'Task.WhatId',
                           'Task.Id',
                           'Email.RelatedToName'])

print(df.columns)
import re
df.rename(columns={col: re.sub(r'\.', r' ', col) for col in df.columns}, inplace=True)
print(df.columns)