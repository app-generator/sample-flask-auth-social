# Flask Social Login 

Open-source Flask Sample built on top of `flask-dance` library. The project implements the social login for Github and Twitter.

> 

- Up-to-date [dependencies](./requirements.txt): **Flask 2.0.1**
- `OPENID` Social login over [Flask Dance](https://pypi.org/project/Flask-Dance/)
  - Github 
  - Twitter
- SQLite Persistence
- Support via **Github** (issues tracker) and [Discord](https://discord.gg/fZC6hup).

<br />

![Flask Social Login - Free sample provided by AppSeed.](https://user-images.githubusercontent.com/51070104/135398234-06a43c1a-cd0a-45ad-accc-de45061d8945.png)

<br />

## Build from sources

> **Step #1** - Clone sources (this repo)

```bash
$ # Clone the sources
$ git clone https://github.com/app-generator/flask-social-login-v2.git
$ cd flask-social-login-v2
```

<br />

> **Step #2** - Create a virtual environment

```bash
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
```

<br />

> **Step #3** - Install dependencies

```bash
$ # Install requirements
$ pip3 install -r requirements.txt
```

<br />

> **Step #4** - Set Up Environment

```bash
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
```

<br />

> **Step #5** - (optional) Enable DEBUG Environment (local development)

```bash
$ # Set up the DEBUG environment
$ (Unix/Mac) export FLASK_ENV=development
$ (Windows) set FLASK_ENV=development
$ (Powershell) $env:FLASK_ENV = "development"
```

<br />

> **Github Setup** - [Creating an OAuth App](https://docs.github.com/en/developers/apps/building-oauth-apps/creating-an-oauth-app)

- SignIN to Github
- Access `Settings` -> `Developer Settings` -> `OAuth Apps`
- Edit your OAuth App
  - `App Name`
  - `App Description`
  - (mandatory) `HomePage`: `https://localhost:5000`
  - (mandatory) `Authorization callback URL`: `https://localhost:5000/login/github/authorized`
  - Generate a new `secret key`

<br />

> **Twitter Setup** - [Creating an OAuth App](https://developer.twitter.com/en/portal/projects-and-apps) 

- SignIN to Twitter
- Access `Developer Section` -> https://developer.twitter.com/en/portal/projects-and-apps
- Create a new APP
- Edit User authentication settings
  - Check `OAuth 1.0a`
  - (mandatory) `HomePage`: `https://localhost:5000`
  - (mandatory) `Authorization callback URL`: `https://localhost:5000/login/twitter/authorized`
  - Generate a new `secret key`

<br />

> **Update Environment** - Rename `.env.sample` to `.env` and edit the file

- For GITHUB Login
  - `GITHUB_ID` - value provided by `Github Setup`
  - `GITHUB_SECRET` - value provided by `Github Setup`
- For TWitter Login
  - `TWITTER_ID` - value provided by `Twitter Setup`
  - `TWITTER_SECRET` - value provided by `Twitter Setup`

<br />

> **Step #8** - Start the project (HTTPS)

```bash
$ flask run --cert=adhoc
$
$ # Access the app: HTTPS://127.0.0.1:5000/
```

**Important:** The `--cert=adhoc` will force the https protocol

<br />

## Account Details

Once the user is authenticated, all available information can be accessed via `/ping` route:

> Github sample (truncated): `https://localhost:5000/ping` 

```json
{
  "avatar_url": "https://avatars.githubusercontent.com/u/51070104?v=4", 
  "bio": "App Generator and Boilerplate Code.", 
  "blog": "https://appseed.us/app-generator", 
  "company": "AppSeed", 
  "created_at": "2019-05-27T04:55:15Z", 
  "followers": 777, 
  "public_repos": 495, 
  "url": "https://api.github.com/users/app-generator"
}
```

<br />

## Credits

- Originally coded by [TestDriven.IO](https://github.com/testdrivenio/flask-social-auth)
- [Flask-Dance](https://flask-dance.readthedocs.io/en/latest/) - The library that implements the hard work  

<br />

--- 
Flask Social Login - Free sample provided by **AppSeed [App Generator](https://appseed.us/app-generator)**.
