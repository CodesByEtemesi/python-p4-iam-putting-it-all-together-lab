# #!/usr/bin/env python3

# from flask import request, session
# from flask_restful import Resource
# from sqlalchemy.exc import IntegrityError

# from config import app, db, api
# from models import User, Recipe

# class Signup(Resource):
#     pass

# class CheckSession(Resource):
#     pass

# class Login(Resource):
#     pass

# class Logout(Resource):
#     pass

# class RecipeIndex(Resource):
#     pass

# api.add_resource(Signup, '/signup', endpoint='signup')
# api.add_resource(CheckSession, '/check_session', endpoint='check_session')
# api.add_resource(Login, '/login', endpoint='login')
# api.add_resource(Logout, '/logout', endpoint='logout')
# api.add_resource(RecipeIndex, '/recipes', endpoint='recipes')


# if __name__ == '__main__':
#     app.run(port=5555, debug=True)

# app.py

# from flask import request, session
# from flask_restful import Resource
# from sqlalchemy.exc import IntegrityError

# from config import app, db, api
# from models import User, Recipe

# class Signup(Resource):
#     pass

# class CheckSession(Resource):
#     pass

# class Login(Resource):
#     pass

# class Logout(Resource):
#     pass

# class RecipeIndex(Resource):
#     pass

# api.add_resource(Signup, '/signup', endpoint='signup')
# api.add_resource(CheckSession, '/check_session', endpoint='check_session')
# api.add_resource(Login, '/login', endpoint='login')
# api.add_resource(Logout, '/logout', endpoint='logout')
# api.add_resource(RecipeIndex, '/recipes', endpoint='recipes')


# if __name__ == '__main__':
#     app.run(port=5555, debug=True)


# app.py

# from flask import request, session, jsonify
# from flask_restful import Resource
# from sqlalchemy.exc import IntegrityError

# from config import app, db, api
# from models import User, Recipe

# class Signup(Resource):
#     def post(self):
#         data = request.get_json()
#         username = data.get('username')
#         password = data.get('password')
#         image_url = data.get('image_url')
#         bio = data.get('bio')

#         if not (username and password):
#             return {'error': 'Username and password are required.'}, 422

#         user = User.query.filter_by(username=username).first()
#         if user:
#             return {'error': 'Username already exists.'}, 422

#         new_user = User(username=username, image_url=image_url, bio=bio)
#         new_user.password_hash = password

#         try:
#             db.session.add(new_user)
#             db.session.commit()
#             session['user_id'] = new_user.id
#             return jsonify(new_user.serialize()), 201
#         except IntegrityError:
#             db.session.rollback()
#             return {'error': 'Error saving user to the database.'}, 422

# class CheckSession(Resource):
#     def get(self):
#         user_id = session.get('user_id')
#         if user_id:
#             user = User.query.get(user_id)
#             return jsonify(user.serialize()), 200
#         else:
#             return {'error': 'User not logged in.'}, 401

# class Login(Resource):
#     def post(self):
#         data = request.get_json()
#         username = data.get('username')
#         password = data.get('password')

#         user = User.query.filter_by(username=username).first()

#         if user and user.check_password(password):
#             session['user_id'] = user.id
#             return jsonify(user.serialize()), 200
#         else:
#             return {'error': 'Invalid username or password.'}, 401

# class Logout(Resource):
#     def delete(self):
#         if 'user_id' in session:
#             session.pop('user_id')
#             return '', 204
#         else:
#             return {'error': 'User not logged in.'}, 401

# class RecipeIndex(Resource):
#     def get(self):
#         user_id = session.get('user_id')
#         if user_id:
#             recipes = Recipe.query.all()
#             return jsonify([recipe.serialize() for recipe in recipes]), 200
#         else:
#             return {'error': 'User not logged in.'}, 401

#     def post(self):
#         user_id = session.get('user_id')
#         if not user_id:
#             return {'error': 'User not logged in.'}, 401

#         data = request.get_json()
#         title = data.get('title')
#         instructions = data.get('instructions')
#         minutes_to_complete = data.get('minutes_to_complete')

#         if not (title and instructions and minutes_to_complete):
#             return {'error': 'Title, instructions, and minutes_to_complete are required.'}, 422

#         new_recipe = Recipe(title=title, instructions=instructions, minutes_to_complete=minutes_to_complete, user_id=user_id)

#         try:
#             db.session.add(new_recipe)
#             db.session.commit()
#             return jsonify(new_recipe.serialize()), 201
#         except IntegrityError:
#             db.session.rollback()
#             return {'error': 'Error saving recipe to the database.'}, 422

# api.add_resource(Signup, '/signup', endpoint='signup')
# api.add_resource(CheckSession, '/check_session', endpoint='check_session')
# api.add_resource(Login, '/login', endpoint='login')
# api.add_resource(Logout, '/logout', endpoint='logout')
# api.add_resource(RecipeIndex, '/recipes', endpoint='recipes')

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)


# app.py

# from flask import request, session, jsonify
# from flask_restful import Resource
# from sqlalchemy.exc import IntegrityError

# from config import app, db, api
# from models import User, Recipe

# class Signup(Resource):
#     def post(self):
#         data = request.get_json()
#         username = data.get('username')
#         password = data.get('password')
#         image_url = data.get('image_url')
#         bio = data.get('bio')

#         if not (username and password):
#             return {'error': 'Username and password are required.'}, 422

#         user = User.query.filter_by(username=username).first()
#         if user:
#             return {'error': 'Username already exists.'}, 422

#         new_user = User(username=username, image_url=image_url, bio=bio)
#         new_user.password_hash = password

#         try:
#             db.session.add(new_user)
#             db.session.commit()
#             session['user_id'] = new_user.id
#             return jsonify(new_user.serialize()), 201
#         except IntegrityError as e:
#             db.session.rollback()
#             return {'error': 'Error saving user to the database.', 'details': str(e)}, 422

# class CheckSession(Resource):
#     def get(self):
#         user_id = session.get('user_id')
#         if user_id:
#             user = User.query.get(user_id)
#             return jsonify(user.serialize()), 200
#         else:
#             return {'error': 'User not logged in.'}, 401

# class Login(Resource):
#     def post(self):
#         data = request.get_json()
#         username = data.get('username')
#         password = data.get('password')

#         user = User.query.filter_by(username=username).first()

#         if user and user.check_password(password):
#             session['user_id'] = user.id
#             return jsonify(user.serialize()), 200
#         else:
#             return {'error': 'Invalid username or password.'}, 401

# class Logout(Resource):
#     def delete(self):
#         if 'user_id' in session:
#             session.pop('user_id')
#             return '', 204
#         else:
#             return {'error': 'User not logged in.'}, 401

# class RecipeIndex(Resource):
#     def get(self):
#         user_id = session.get('user_id')
#         if user_id:
#             recipes = Recipe.query.filter_by(user_id=user_id).all()
#             return jsonify([recipe.serialize() for recipe in recipes]), 200
#         else:
#             return {'error': 'User not logged in.'}, 401

#     def post(self):
#         user_id = session.get('user_id')
#         if not user_id:
#             return {'error': 'User not logged in.'}, 401

#         data = request.get_json()
#         title = data.get('title')
#         instructions = data.get('instructions')
#         minutes_to_complete = data.get('minutes_to_complete')

#         if not (title and instructions and minutes_to_complete):
#             return {'error': 'Title, instructions, and minutes_to_complete are required.'}, 422

#         new_recipe = Recipe(title=title, instructions=instructions, minutes_to_complete=minutes_to_complete, user_id=user_id)

#         try:
#             db.session.add(new_recipe)
#             db.session.commit()
#             return jsonify(new_recipe.serialize()), 201
#         except IntegrityError as e:
#             db.session.rollback()
#             return {'error': 'Error saving recipe to the database.', 'details': str(e)}, 422

# api.add_resource(Signup, '/signup', endpoint='signup')
# api.add_resource(CheckSession, '/check_session', endpoint='check_session')
# api.add_resource(Login, '/login', endpoint='login')
# api.add_resource(Logout, '/logout', endpoint='logout')
# api.add_resource(RecipeIndex, '/recipes', endpoint='recipes')

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)


# app.py

from flask import request, session, jsonify
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from config import app, db, api
from models import User, Recipe

class Signup(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        image_url = data.get('image_url')
        bio = data.get('bio')

        if not (username and password):
            return {'error': 'Username and password are required.'}, 422

        user = User.query.filter_by(username=username).first()
        if user:
            return {'error': 'Username already exists.'}, 422

        new_user = User(username=username, image_url=image_url, bio=bio)
        new_user.set_password(password)

        try:
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            return jsonify(new_user.serialize()), 201
        except IntegrityError as e:
            db.session.rollback()
            return {'error': 'Error saving user to the database.', 'details': str(e)}, 422

class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        if user_id:
            user = User.query.get(user_id)
            return jsonify(user.serialize()), 200
        else:
            return {'error': 'User not logged in.'}, 401

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            return jsonify(user.serialize()), 200
        else:
            return {'error': 'Invalid username or password.'}, 401

class Logout(Resource):
    def delete(self):
        if 'user_id' in session:
            session.pop('user_id')
            return '', 204
        else:
            return {'error': 'User not logged in.'}, 401

class RecipeIndex(Resource):
    def get(self):
        user_id = session.get('user_id')
        if user_id:
            user = User.query.get(user_id)
            recipes = Recipe.query.filter_by(user_id=user_id).all()
            return jsonify([recipe.serialize() for recipe in recipes]), 200
        else:
            return {'error': 'User not logged in.'}, 401

    def post(self):
        user_id = session.get('user_id')
        if not user_id:
            return {'error': 'User not logged in.'}, 401

        data = request.get_json()
        title = data.get('title')
        instructions = data.get('instructions')
        minutes_to_complete = data.get('minutes_to_complete')

        if not (title and instructions and minutes_to_complete):
            return {'error': 'Title, instructions, and minutes_to_complete are required.'}, 422

        new_recipe = Recipe(title=title, instructions=instructions, minutes_to_complete=minutes_to_complete, user_id=user_id)

        try:
            db.session.add(new_recipe)
            db.session.commit()
            return jsonify(new_recipe.serialize()), 201
        except IntegrityError as e:
            db.session.rollback()
            return {'error': 'Error saving recipe to the database.', 'details': str(e)}, 422

api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(RecipeIndex, '/recipes', endpoint='recipes')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
