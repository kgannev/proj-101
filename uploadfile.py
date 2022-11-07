import os
import dropbox 


class TransferData:
    def_init_(self,access_token):
        self.access_token = access_token

    def uploadfile(self, file_from, file_to):
    
        dbx = dropbox.Dropbox(self,access_token)

        for root, dirs. files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root,filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path =  os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                   dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
   
   def main():
       access_token = 'BSq8kgc9PJJItnFFUQhj5XmxAt3tAooU8iHd1Q3j-FPiYGW8lWjihnFGP6JVVfvAedHUbR2eawu50glIBTaNqao1UJWWeambTw9NfzuMA536DRzUeWOOtSz_ePG-g7YMFz8P4sg'
       transferData = TransferData(access_token)

       file_from = input("Enter the file path to transfer:- ")
       file_to = input("enter the full path to upload to dropbox:- ")

       transferData.upload_file(file_from,file_to) 
       print(" file has been moved !!!")

    main()
          