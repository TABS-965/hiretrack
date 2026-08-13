from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__)
app.config["SECRET_KEY"] = "hiretrack-demo-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{BASE_DIR / 'hiretrack.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(160), nullable=False)
    location = db.Column(db.String(120), default="Remote")
    status = db.Column(db.String(30), default="Applied")
    date_applied = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    notes = db.Column(db.Text, default="")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id, "company": self.company, "role": self.role,
            "location": self.location, "status": self.status,
            "date_applied": self.date_applied.isoformat(),
            "notes": self.notes
        }

def seed_database():
    if Application.query.count() == 0:
        demo = [
            Application(company="DecodeLabs", role="Full-Stack Developer", location="Karachi", status="Interview", notes="Technical interview scheduled."),
            Application(company="Systems Limited", role="Software Engineer", location="Lahore", status="Applied", notes="Resume submitted through careers portal."),
            Application(company="10Pearls", role="Frontend Developer", location="Islamabad", status="Offer", notes="Offer received — review package."),
            Application(company="Contour Software", role="Junior Software Engineer", location="Lahore", status="Rejected", notes="Keep improving system design skills."),
            Application(company="NETSOL Technologies", role="Python Developer", location="Karachi", status="Applied", notes="Follow up next week.")
        ]
        db.session.add_all(demo)
        db.session.commit()

@app.route("/")
def index():
    applications = Application.query.order_by(Application.date_applied.desc()).all()
    stats = {
        "total": len(applications),
        "applied": sum(a.status == "Applied" for a in applications),
        "interview": sum(a.status == "Interview" for a in applications),
        "offer": sum(a.status == "Offer" for a in applications),
        "rejected": sum(a.status == "Rejected" for a in applications),
    }
    responded = stats["interview"] + stats["offer"] + stats["rejected"]
    stats["response_rate"] = round((responded / stats["total"]) * 100) if stats["total"] else 0
    return render_template("index.html", applications=applications, stats=stats)

@app.post("/applications")
def create_application():
    company = request.form.get("company", "").strip()
    role = request.form.get("role", "").strip()
    location = request.form.get("location", "").strip() or "Remote"
    status = request.form.get("status", "Applied")
    date_raw = request.form.get("date_applied", "")
    notes = request.form.get("notes", "").strip()

    if not company or not role:
        flash("Company and role are required.", "error")
        return redirect(url_for("index"))

    try:
        applied_date = datetime.strptime(date_raw, "%Y-%m-%d").date() if date_raw else datetime.utcnow().date()
    except ValueError:
        applied_date = datetime.utcnow().date()

    db.session.add(Application(
        company=company, role=role, location=location,
        status=status, date_applied=applied_date, notes=notes
    ))
    db.session.commit()
    flash("Application added successfully.", "success")
    return redirect(url_for("index"))

@app.post("/applications/<int:application_id>/update")
def update_application(application_id):
    app_item = Application.query.get_or_404(application_id)
    app_item.status = request.form.get("status", app_item.status)
    app_item.notes = request.form.get("notes", app_item.notes)
    db.session.commit()
    flash("Application updated.", "success")
    return redirect(url_for("index"))

@app.post("/applications/<int:application_id>/delete")
def delete_application(application_id):
    app_item = Application.query.get_or_404(application_id)
    db.session.delete(app_item)
    db.session.commit()
    flash("Application removed.", "success")
    return redirect(url_for("index"))

@app.get("/api/applications")
def api_applications():
    return jsonify([a.to_dict() for a in Application.query.order_by(Application.date_applied.desc()).all()])

@app.get("/health")
def health():
    return {"status": "ok", "service": "HireTrack"}

with app.app_context():
    db.create_all()
    seed_database()

if __name__ == "__main__":
    app.run(debug=True)
