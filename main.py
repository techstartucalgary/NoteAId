from flask import Flask #importing flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with #modules import
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #making a new Flask App
api = Api(app) #wrap App in an API -> using RESTful API
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model): 
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	views = db.Column(db.Integer, nullable=False)
	likes = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Video(name = {name}, views = {views}, likes = {likes})"

video_put_args = reqparse.RequestParser() 
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
#help is an error message
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video is required")
video_update_args.add_argument("views", type=int, help="Views of the video")
video_update_args.add_argument("likes", type=int, help="Likes on the video")

resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'views': fields.Integer,
	'likes': fields.Integer
}


class Video(Resource):  # making a class that is a resource
	@marshal_with(resource_fields)
	def get(self, video_id): #get_request
		result = VideoModel.query.filter_by(id=video_id).first()
		if not result:
			abort(404, message="Could not find video with that id")
		return result

	@marshal_with(resource_fields)
	def put(self, video_id): #video_id is a parameter 
        #creating a new video 
		args = video_put_args.parse_args() #check if all args are present 
		result = VideoModel.query.filter_by(id=video_id).first()
		if result:
			abort(409, message="Video id taken...")

		video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
		db.session.add(video)
		db.session.commit()
		return video, 201

	@marshal_with(resource_fields)
	def patch(self, video_id):
		args = video_update_args.parse_args()
		result = VideoModel.query.filter_by(id=video_id).first()
		if not result:
			abort(404, message="Video doesn't exist, cannot update")

		if args['name']:
			result.name = args['name']
		if args['views']:
			result.views = args['views']
		if args['likes']:
			result.likes = args['likes']

		db.session.commit()

		return result


	def delete(self, video_id):
		abort_if_video_id_doesnt_exist(video_id)
		del videos[video_id]
		return '', 204


api.add_resource(Video, "/video/<int:video_id>") #registiring Video class as resource
#making it accessible to API
#"/video/<int:video_id>" is root of resource -> will be accesible here
# if sending a get request to "/video/<int:video_id>" it will run class Video and

#always at the bottom
if __name__ == "__main__": 
	app.run(debug=True) #start servers + start flask app
    #it is in debug mode, dont do debug is true in production only in dev
