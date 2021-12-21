import os
import secrets
from PIL import Image
from flask import render_template,url_for, flash, redirect, request, abort
from FMagdum import app, db, bcrypt, mail
from FMagdum.forms import (RegistrationForm, LoginForm, UpdateAccountForm, 
                            PostForm, RequestResetForm, ResetPasswordForm)
from FMagdum.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
from FMagdum.__init__ import mail

assert 'SYSTEMROOT' in os.environ









