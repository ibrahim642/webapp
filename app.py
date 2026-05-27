#!/usr/bin/env python3
"""
Flask web application for family leave management
"""

import os
from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from models import db, FamilyMember, Leave

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-change-this'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///family_leaves.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    """Load user by id"""
    return FamilyMember.query.get(int(user_id))


@app.route('/')
def index():
    """Home page route"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page and authentication"""
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        
        member = FamilyMember.query.filter_by(name=name).first()
        
        if member and member.check_password(password):
            login_user(member)
            flash(f'Welcome back, {member.name}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid name or password', 'danger')
    
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    """Logout user"""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    """Dashboard showing all family leaves"""
    all_leaves = Leave.query.order_by(Leave.start_date).all()
    
    # Group leaves by member for easier viewing
    leaves_by_member = {}
    for leave in all_leaves:
        if leave.member.name not in leaves_by_member:
            leaves_by_member[leave.member.name] = []
        leaves_by_member[leave.member.name].append(leave)
    
    return render_template('dashboard.html', 
                          leaves_by_member=leaves_by_member,
                          all_leaves=all_leaves)


@app.route('/my-leaves')
@login_required
def my_leaves():
    """Show current user's leaves"""
    my_leaves = Leave.query.filter_by(member_id=current_user.id).order_by(Leave.start_date).all()
    return render_template('my_leaves.html', leaves=my_leaves)


@app.route('/add-leave', methods=['GET', 'POST'])
@login_required
def add_leave():
    """Add a new leave"""
    if request.method == 'POST':
        try:
            start_date = datetime.strptime(request.form.get('start_date'), '%Y-%m-%d').date()
            end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d').date()
            leave_type = request.form.get('leave_type')
            reason = request.form.get('reason')
            
            if start_date > end_date:
                flash('Start date must be before end date', 'danger')
                return redirect(url_for('add_leave'))
            
            leave = Leave(
                member_id=current_user.id,
                leave_type=leave_type,
                start_date=start_date,
                end_date=end_date,
                reason=reason
            )
            
            db.session.add(leave)
            db.session.commit()
            
            flash(f'Leave added successfully from {start_date} to {end_date}', 'success')
            return redirect(url_for('dashboard'))
        
        except ValueError as e:
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('add_leave.html')


@app.route('/edit-leave/<int:leave_id>', methods=['GET', 'POST'])
@login_required
def edit_leave(leave_id):
    """Edit an existing leave"""
    leave = Leave.query.get_or_404(leave_id)
    
    # Check if user owns this leave
    if leave.member_id != current_user.id:
        flash('You can only edit your own leaves', 'danger')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        try:
            leave.start_date = datetime.strptime(request.form.get('start_date'), '%Y-%m-%d').date()
            leave.end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d').date()
            leave.leave_type = request.form.get('leave_type')
            leave.reason = request.form.get('reason')
            
            if leave.start_date > leave.end_date:
                flash('Start date must be before end date', 'danger')
                return redirect(url_for('edit_leave', leave_id=leave_id))
            
            db.session.commit()
            flash('Leave updated successfully', 'success')
            return redirect(url_for('dashboard'))
        
        except ValueError as e:
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('edit_leave.html', leave=leave)


@app.route('/delete-leave/<int:leave_id>', methods=['POST'])
@login_required
def delete_leave(leave_id):
    """Delete a leave"""
    leave = Leave.query.get_or_404(leave_id)
    
    # Check if user owns this leave
    if leave.member_id != current_user.id:
        flash('You can only delete your own leaves', 'danger')
        return redirect(url_for('dashboard'))
    
    db.session.delete(leave)
    db.session.commit()
    
    flash('Leave deleted successfully', 'success')
    return redirect(url_for('dashboard'))


@app.route('/api/hello')
def api_hello():
    """API endpoint that returns a JSON response"""
    return {'message': 'Hello from the Flask API!'}


def init_db():
    """Initialize the database with sample family members"""
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Check if members already exist
        if FamilyMember.query.count() == 0:
            # Create sample family members
            members = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry']
            
            for name in members:
                member = FamilyMember(name=name)
                member.set_password('password123')  # Default password for demo
                db.session.add(member)
            
            db.session.commit()
            print(f"Created {len(members)} family members with default password 'password123'")


if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
