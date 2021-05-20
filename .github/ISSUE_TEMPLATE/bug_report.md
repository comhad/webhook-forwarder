---
name: Bug report
about: Create a report to help us improve and get rid of bugs
title: ''
labels: ''
assignees: comhad

---

**Before you report a bug, test the link**
To test your URL, open your CMD or terminal and run 
```curl -H 'Content-Type: application/json'  --data '{ "content" : "test" }'```
followed by a space and your URL with no `?msg=` on the end of it, you should receive a response that looks like
```{"message":"success","status":200,"webhookStatus":204}```
and a message will be posted in the channel where your webhook is located. This proves your URL is correctly formatted.

If you receive a response that looks like
```{"message":"success","status":200,"webhookStatus":401}```
then the URL is incorrectly formatted and you did not input the webhook link correctly, refer to the README for info on how to do that.

**Describe the bug**
A clear and concise description of what the bug is.

**URL you use**
Give the steps to reproduce this error, if you want to post the URL that's fine but you should censor it or delete it in discord before you post it here. 

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Websites or services you are using**
Mention any websites and plugins you are using which might potentially interfere with the URL

**Additional context**
Add any other context about the problem here.
