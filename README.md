# PROJECT DESCRIPTION

Minimalistic portfolio of stuttering czech copywriter Vojtěch Hulinský with its own custom developed content management system.<br/>
<a href="kocopywriter.cz">kocopywriter.cz</a>

## Technologies / Stack
### Frontend
- Vue 3 Composition API, Typescript
- CSS
- Pinia, Axios, Vue Router, Tiptap, NotificationQuark, LoaderQuark, Swiper

### Backend
- FastAPI, Python
- SQLAlchemy

### Database
- PostgreSQL


# LOCAL SETUP
### Frontend
1. Clone the repository and install dependencies in the /frontend.
```sh
npm install
```
2. Change the base url based to point on your running backend server in the file <b>frontend/lib/endpoints.ts</b>
3. Run the frontend server
```sh
npm run dev
```


### Backend
1. Clone the repository and install dependencies in the /backend:
```sh
pip install -r requirements.txt
```
2. Setup postgres database, you can use the provided docker-compose file or some online tutorial.

3. Change the <b>backend/core/config.py</b> according to your needs.

4. Run the backend server:
```sh
python3 run.py
```


# DEVELOPMENT / CONTRIBUTION

If you want to make changes, clone the repository and follow the setup instructions. <br/>
**Then create your own branch and make pull request with your changes.**  <br/>
After that, I will review your changes and merge them into the main branch. <br/>
By that, the website is already automatically rebuild and updated on the live server. 


PS: Do not push config files with your local setup.