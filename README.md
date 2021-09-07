## product name - spotify set go


### what is this?
a script to tweet song info about songs i am currently listening to on spotify

### why did i build this?
why not?


### want to use it?

* clone the repo
```
gh repo clone dibrinsofor/readme-template
```
* create a file ".env" and store all of your twitter and spotify credentials
* that's it! you can run it now and watch it go.
```
python app.py
```

### how it works
i got to learn how to use two python libraries to make requests to the spotify and twitter APIs: tekore and tweepy. once you setup your .env variables, the app makes an Oauth request (to authenticate your spotify account) and just listens to hear what song you're currently listening to and tweets the song info because you are clearly not spamming your friends enough

#### technologies
this was built entirely with love over the span of a year because i got bored:

- python
- twitter and spotify APIs
- <3

### what's coming next
idk... i think it'll be cool for it to tweet the url of the song too and i'll still need to clean up the code

### want to help make this better?
thank you. just reach out to me if you need any additional help

[//]: # (So depending on use case, you may want to keep the documentation short. in that case you may not need to include the last two sections or you can)
