# kaj-bot

[u/kaj-bot](https://www.reddit.com/user/kaj-bot) lurks around on the [r/kjfacts](https://www.reddit.com/r/kjfacts/) subreddit and replies to comments that invoke its name with a [kj-fact](https://github.com/knekvasil/kj-facts) from the kjfacts API. 

Try it for yourself!


### Quick deployment reminder

Heroku has different deployment types. Because this is a background script and not a web app, the deployment type must be: *worker*.

#### Because I will probably forget...

`$ docker build -t <image name> -f Dockerfile .`

`$ docker tag <image name> registry.heroku.com/<Heroku app name>/worker`

`$ docker push registry.heroku.com/<Heroku app name>/worker`

`$ heroku container:release worker -a <Heroku app name>`
