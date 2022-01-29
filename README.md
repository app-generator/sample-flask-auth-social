# Flask Social Login

Open-source Flask sample built on top of `flask-dance` library. The project showcases the social login for Github - Features: 

- Up-to-date [dependencies](./requirements.txt): **Flask 2.0.1**
- `OPENID` Social login over [Flask Dance](https://pypi.org/project/Flask-Dance/)
  - Github Login
  - Google Login (WIP) 
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

> **Step #5** - [Creating an OAuth App](https://docs.github.com/en/developers/apps/building-oauth-apps/creating-an-oauth-app) (on Github)

- SignIN to Github
- Access `Settings` -> `Developer Settings` -> `OAuth Apps`
- Edit your OAuth App
  - `App Name`
  - `App Description`
  - (mandatory) `HomePage`: `https://localhost:5000`
  - (mandatory) `Authorization callback URL`: `https://localhost:5000/login/github/authorized`
  - Generate a new `secret key`

<br />

> **Step #6** - Rename `.env.sample` to `.env` and edit the file

- `GITHUB_OAUTH_CLIENT_ID` - value provided by Github (step #5)
- `GITHUB_OAUTH_CLIENT_SECRET` - value provided by Github (step #5)

<br />

> **Step #7** - (optional) Enable DEBUG Environment (local development)

```bash
$ # Set up the DEBUG environment
$ (Unix/Mac) export FLASK_ENV=development
$ (Windows) set FLASK_ENV=development
$ (Powershell) $env:FLASK_ENV = "development"
```

<br />

> **Step #8** - Start the project (HTTPS)

```bash
$ flask run --cert=adhoc
$
$ # Access the app in browser: HTTPS://127.0.0.1:5000/
```

<br />

---

Flask Social Login - Free sample provided by **AppSeed [App Generator](https://appseed.us/app-generator)**.
