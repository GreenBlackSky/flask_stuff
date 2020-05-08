from flask import Blueprint, render_template


admin_bp = Blueprint(
    'admin_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@admin_bp.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template(
        'dashboard.html',
        title='Admin Dashboard',
        template='dashboard-static account',
        body="Account"
    )