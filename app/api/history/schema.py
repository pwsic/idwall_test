from flask_restx import fields

history_post_schema = {
    "id": fields.String,
    "initialDate": fields.String,
    "finalDate": fields.String,
}
