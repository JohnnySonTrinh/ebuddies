# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

Welcome to the Ebuddies Site testing results, in this file you will see how each and every element and features tested to ensure each features worked as intended.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my pages.

| Page | Screenshot | Notes |
| ---- | ---------- | ----- |
| [Home](https://ebuddies-42967ce5447d.herokuapp.com/) | ![screenshot](documentation/validation/html-home.png) | [ERROR] Bad Value |
| [Log-in](https://ebuddies-42967ce5447d.herokuapp.com/login/) | ![screenshot](documentation/validation/html-login.png) | [NO ERROR] |
| [Register](https://ebuddies-42967ce5447d.herokuapp.com/register/) | ![screenshot](documentation/validation/html-register.png) | [ERROR] 3 The aria-describedby attribute must point to an element in the same document.|
| [Topics](https://ebuddies-42967ce5447d.herokuapp.com/topics/) | ![screenshot](documentation/validation/html-topics.png) | [ERROR] Bad value |
| [Profile](https://ebuddies-42967ce5447d.herokuapp.com/profile/1/) | ![screenshot](documentation/validation/html-profile.png) | [ERROR] Bad value |
| [Thread](https://ebuddies-42967ce5447d.herokuapp.com/thread/8/) | ![screenshot](documentation/validation/html-thread.png) | [NO ERROR] |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Local | Live | Notes |
| --- | --- | --- |
| ![screenshot](documentation/validation/css-local.png) | ![screenshot](documentation/validation/css-live.png) | Only warrnings -webkit [Local] import fonts warrning |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | script.js | ![screenshot](documentation/validation/js-jshint.png) | No Error |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| base | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JohnnySonTrinh/ebuddies/main/base/admin.py) | ![screenshot](documentation/validation/py-admin.png) | NO ERRORS |
| base | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JohnnySonTrinh/ebuddies/main/base/forms.py) | ![screenshot](documentation/validation/py-forms.png) | NO ERRORS |
| base | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JohnnySonTrinh/ebuddies/main/base/models.py) | ![screenshot](documentation/validation/py-models.png) | NO ERRORS |
| base | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JohnnySonTrinh/ebuddies/main/base/urls.py) | ![screenshot](documentation/validation/py-urls.png) | NO ERRORS |
| base | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JohnnySonTrinh/ebuddies/main/base/views.py) | ![screenshot](documentation/validation/py-views.png) | NO ERRORS |
| ebuddies | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JohnnySonTrinh/ebuddies/main/ebuddies/urls.py) | ![screenshot](documentation/validation/py-urls-ebuddies.png) | NO ERRORS |
| root | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JohnnySonTrinh/ebuddies/main/manage.py) | ![screenshot](documentation/validation/py-manage.png) |NO ERRORS |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Profile | Log In | Register | Thread | Topic | Notes |
| ------- | ---- | ------- | ------ | -------- | ------ | ----- | ----- |
| Chrome | ![screenshot](documentation/browsers/chrome-home.png) | ![screenshot](documentation/browsers/chrome-profile.png) | ![screenshot](documentation/browsers/chrome-login.png) | ![screenshot](documentation/browsers/chrome-signup.png) | ![screenshot](documentation/browsers/chrome-thread.png) | ![screenshot](documentation/browsers/chrome-topics.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/firefox-home.png) | ![screenshot](documentation/browsers/firefox-profile.png) | ![screenshot](documentation/browsers/firefox-login.png) | ![screenshot](documentation/browsers/firefox-signup.png) | ![screenshot](documentation/browsers/firefox-thread.png) | ![screenshot](documentation/browsers/firefox-topics.png) | Works as expected |
| Opera GX | ![screenshot](documentation/browsers/opera-gx-home.png) | ![screenshot](documentation/browsers/opera-gx-profile.png) | ![screenshot](documentation/browsers/opera-gx-login.png) | ![screenshot](documentation/browsers/opera-gx-signup.png) | ![screenshot](documentation/browsers/opera-gx-thread.png) | ![screenshot](documentation/browsers/opera-gx-topics.png) | Works as expected |
| Safari | ![screenshot](documentation/browsers/safari-home.png) | ![screenshot](documentation/browsers/safari-profile.png) | ![screenshot](documentation/browsers/safari-login.png) | ![screenshot](documentation/browsers/safari-signup.png) | ![screenshot](documentation/browsers/safari-thread.png) | ![screenshot](documentation/browsers/safari-topics.png) | Works as expected |

