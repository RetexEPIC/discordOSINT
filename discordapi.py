import os
print("Enter invite code: ", end='')
invite = input()
os.system("curl https://discord.com/api/v9/invites/" + invite)