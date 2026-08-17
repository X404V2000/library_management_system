import datetime
import os
import requests
import json
from fastapi import FastAPI, HTTPException
from apiCall import InvalidOperationResponse, ValidOperationResponse

app = FastAPI()

def externalErrorHandling_False():
    ##error handling response from an external source code
    ##for any invalid user error return 'invalidResponse'
    invalidResponse = InvalidOperationResponse.usrDisplay(
            400,
            "Bad Request",
            "Server cannot process the request"
    )

def externalErrorHandling_True():
    ##for any valid user error return 'validResponse'
    validResponse = ValidOperationResponse.usrDisplay(
            200,
            "OK",
            "The request was successful"
    )

def menu():
    print("="*60 + "\nLibrary Management System\n" + "="*60)
    print("[1]. Search Book")
    print("[2]. Add Book")
    print("[3]. Cataloging")
    print("[4]. Classification")
    print("[5]. Exit")
    print("="*60)

def main():
    while True:
        menu()
        try:
            menu_arg = int(input("Choose Option ... 1-4: "))
        except ValueError:
            print("\n")
            externalErrorHandling_False()
            print("Invalid input ... Choose option 1-5")
            print("\n")
            continue
        

        if menu_arg == 1:
            print("testing")        #temporary until testing is complete
            externalErrorHandling_True()
        elif menu_arg == 2:
            print("testing")        #temporary until testing is complete

        elif menu_arg == 3:
            print("testing")        #temporary until testing is complete

        elif menu_arg == 4:
            print("testing")        #temporary until testing is complete

        elif menu_arg == 5:
            print("testing")        #temporary until testing is complete

        else:
            print("\n")
            externalErrorHandling_False()
            input("Press Enter to continue")
            print("\n")
            continue
    
if __name__ == "__main__":
    main()
