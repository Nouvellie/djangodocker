__author__      =     "Rocuant Roberto"
__created__     =     "07/21/2021" # MM/DD/YYYY
__credits__     =     None
__copyright__   =     None
__email__       =     "roberto.rocuantv@gmail.com"
__maintainer__  =     "Rocuant Roberto"
__prod__        =     None
__structure__   =     "str(version) - str(date) - list(info) - list(problems) - none-bool(fixed) - str(commit) - none-bool(prod)"
__version__     =     "0.1.0"
__logs__        =  {
    'version':      "0.1.0",
    'date':         "07/23/2021",
    'info':         ["Docker with Gunicorn and Nginx.", "Dockerfile, compose and sh for build created.", "Last version of docker and sub components."],
    'problems':     ["",],
    'fixed':        None,
    'commit':       "",
    "prod":         None,
}

# __logs__        =  {
#     'version':      "0.0.4",
#     'date':         "07/22/2021",
#     'info':         ["SignInView custom.", "Fix Tokens views.", "Adapted Verified token models.", "Serializers VerifiedAccount models."],
#     'problems':     ["",],
#     'fixed':        None,
#     'commit':       "",
#     "prod":         None,
# }

# __logs__        =  {
#     'version':      "0.0.3",
#     'date':         "07/22/2021",
#     'info':         ["Refresh access token with refresh token ready.", "Check refresh token with refresh token ready.", "Check refresh token with credentials ready.",],
#     'problems':     ["",],
#     'fixed':        None,
#     'commit':       "",
#     "prod":         None,
# }

# __logs__        =  {
#     'version':      "0.0.2",
#     'date':         "07/22/2021",
#     'info':         ["Check Token with credentials or refresh token.", "Custom validations from JWT library adapted.", "Get last token.", "Bool for expire date."],
#     'problems':     ["",],
#     'fixed':        None,
#     'commit':       "",
#     "prod":         None,
# }

# __logs__        =  {
#     'version':      "0.0.1",
#     'date':         "07/21/2021",
#     'info':         ["Project start.", "JWT Token added.", "Django environ used.", "Pip requirements.", "StartAPIView added.", "Token adapted to nouvellie headers.",],
#     'problems':     ["",],
#     'fixed':        None,
#     'commit':       "",
#     "prod":         None,
# }

full_info = {
	'__author__': __author__,
	'__created__': __created__,
	'__credits__': __credits__,
	'__copyright__': __copyright__,
	'__email__': __email__,
	'__logs__': __logs__,
	'__maintainer__': __maintainer__,
    '__prod__': __prod__,
	'__version__': __version__,	
}

class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

info = dotdict(dict=full_info)['dict']