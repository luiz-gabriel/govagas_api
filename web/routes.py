from flask import Flask, abort
from dotenv import load_dotenv
import os
#Implementation of control classes and request validation
from Validate.ParametersValidate import Validate as valid
from Request.Data import Data

#Controllers
from Controller.InsertJob import InsertJob
from Controller.DescriptionJob import Description
from Controller.Search import SearchController
from Controller.DetailsOfJob import DetailsOfJobController

class Routes:
    app = Flask(__name__)
    load_dotenv()

    @app.get('/search/page/<int:page>')
    def jobs(page=0):
        data = Data.values()
        
        title = data['title'] if 'title' in data else None
        state = data['state'] if 'state' in data else None
        city = data['city'] if 'city' in data else None

        return SearchController.getJobs(title, state, city, page)

    @app.get('/job/description/<string:slug>')
    def getJob(slug):
        return Description.getData(slug)

    @app.get('/job/details/<string:slug>')
    def jobDetails(slug):
        return DetailsOfJobController.run(slug)
        
    @app.post("/job")
    def job():
        
        data = Data.values()
        if 'private' in data:
            if data['private'] != os.getenv('PRIVATE_REGISTER_KEY'):
                abort(401)
            else:

                valid.validation(data, {
                    "title": {"min": 5, "max": 160}, 
                    "resume": {"min": 20, "max": 120},
                    "description": {"min": 30, "max": 9600},
                    "type": {"min": 5, "max": 64}, 
                    "state": {"min": 2, "max": 2}, 
                    "city": {"min": 5, "max": 64},
                    "link": {"min": 30, "max": 450},
                })
                
                return InsertJob.run(data)
        else:
            abort(401)

    @app.errorhandler(401)
    def handler_401(msg):
        return {"error": str(msg)}, 401

    @app.errorhandler(500)
    def handler_500(msg):
        return {}, 500

    app.run(debug=True, host='0.0.0.0', port=8082)

   