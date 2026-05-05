from flask import Flask, render_template_string

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Healthcare System</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; background: #f0f4f8; }
        .header { background: #0066cc; color: white; padding: 20px 40px; display: flex; align-items: center; gap: 15px; }
        .header h1 { font-size: 24px; }
        .header p { font-size: 13px; opacity: 0.8; }
        .container { max-width: 1100px; margin: 30px auto; padding: 0 20px; }
        .cards { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 30px; }
        .card { background: white; border-radius: 10px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        .card .num { font-size: 32px; font-weight: bold; color: #0066cc; }
        .card .label { font-size: 13px; color: #666; margin-top: 5px; }
        .card .change { font-size: 12px; color: #28a745; margin-top: 4px; }
        .section { background: white; border-radius: 10px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 20px; }
        .section h2 { font-size: 16px; font-weight: bold; margin-bottom: 15px; color: #333; border-bottom: 2px solid #0066cc; padding-bottom: 8px; }
        table { width: 100%; border-collapse: collapse; font-size: 13px; }
        th { background: #f8f9fa; padding: 10px 12px; text-align: left; color: #555; font-weight: 600; border-bottom: 1px solid #eee; }
        td { padding: 10px 12px; border-bottom: 1px solid #f0f0f0; color: #333; }
        tr:hover { background: #f8fbff; }
        .badge { padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 600; }
        .badge-green { background: #d4edda; color: #155724; }
        .badge-red { background: #f8d7da; color: #721c24; }
        .badge-yellow { background: #fff3cd; color: #856404; }
        .badge-blue { background: #cce5ff; color: #004085; }
        .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        .security-item { display: flex; align-items: center; gap: 10px; padding: 10px 0; border-bottom: 1px solid #f0f0f0; font-size: 13px; }
        .security-item:last-child { border-bottom: none; }
        .dot { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }
        .dot-green { background: #28a745; }
        .dot-red { background: #dc3545; }
        .dot-yellow { background: #ffc107; }
        .security-label { flex: 1; color: #333; }
        .pipeline { display: flex; align-items: center; gap: 0; margin: 10px 0; }
        .pipe-step { background: #e8f4fd; border: 1px solid #bee3f8; border-radius: 6px; padding: 8px 14px; font-size: 12px; color: #2c7be5; font-weight: 600; white-space: nowrap; }
        .pipe-arrow { color: #aaa; font-size: 18px; padding: 0 6px; }
        .pipe-step.done { background: #d4edda; border-color: #c3e6cb; color: #155724; }
        .pipe-step.warn { background: #fff3cd; border-color: #ffeeba; color: #856404; }
        .alert-box { background: #fff3cd; border-left: 4px solid #ffc107; padding: 12px 16px; border-radius: 6px; font-size: 13px; color: #856404; margin-bottom: 10px; }
        .footer { text-align: center; padding: 20px; font-size: 12px; color: #999; }
    </style>
</head>
<body>

<div class="header">
    <div>
        <h1>🏥 SecureHealth — DevSecOps Dashboard</h1>
        <p>Healthcare Management System — HIPAA Compliant | DevSecOps Enabled</p>
    </div>
</div>

<div class="container">

    <!-- Stats Cards -->
    <div class="cards">
        <div class="card">
            <div class="num">1,284</div>
            <div class="label">Total Patients</div>
            <div class="change">↑ 12 new today</div>
        </div>
        <div class="card">
            <div class="num">47</div>
            <div class="label">Active Admissions</div>
            <div class="change">↑ 3 since yesterday</div>
        </div>
        <div class="card">
            <div class="num">98.6%</div>
            <div class="label">System Uptime</div>
            <div class="change">Last 30 days</div>
        </div>
        <div class="card">
            <div class="num">0</div>
            <div class="label">Security Incidents</div>
            <div class="change" style="color:#0066cc">All systems secure</div>
        </div>
    </div>

    <!-- DevSecOps Pipeline -->
    <div class="section">
        <h2>CI/CD Security Pipeline Status</h2>
        <div class="pipeline">
            <div class="pipe-step done">✓ Code Commit</div>
            <div class="pipe-arrow">→</div>
            <div class="pipe-step done">✓ SAST Scan</div>
            <div class="pipe-arrow">→</div>
            <div class="pipe-step done">✓ Build Image</div>
            <div class="pipe-arrow">→</div>
            <div class="pipe-step done">✓ Trivy Scan</div>
            <div class="pipe-arrow">→</div>
            <div class="pipe-step done">✓ Push ECR</div>
            <div class="pipe-arrow">→</div>
            <div class="pipe-step done">✓ Deploy K8s</div>
            <div class="pipe-arrow">→</div>
            <div class="pipe-step done">✓ Live</div>
        </div>
    </div>

    <div class="two-col">

        <!-- Patient Records -->
        <div class="section">
            <h2>Recent Patient Records</h2>
            <table>
                <tr>
                    <th>Patient ID</th>
                    <th>Name</th>
                    <th>Department</th>
                    <th>Status</th>
                </tr>
                <tr><td>P-1042</td><td>Arjun Sharma</td><td>Cardiology</td><td><span class="badge badge-green">Stable</span></td></tr>
                <tr><td>P-1041</td><td>Priya Nair</td><td>Neurology</td><td><span class="badge badge-yellow">Monitoring</span></td></tr>
                <tr><td>P-1040</td><td>Ravi Kumar</td><td>Orthopedics</td><td><span class="badge badge-green">Discharged</span></td></tr>
                <tr><td>P-1039</td><td>Meena Iyer</td><td>ICU</td><td><span class="badge badge-red">Critical</span></td></tr>
                <tr><td>P-1038</td><td>Suresh Babu</td><td>General</td><td><span class="badge badge-green">Stable</span></td></tr>
            </table>
        </div>

        <!-- Security Status -->
        <div class="section">
            <h2>Security & Compliance Status</h2>
            <div class="security-item"><div class="dot dot-green"></div><div class="security-label">HIPAA Compliance Check</div><span class="badge badge-green">Passed</span></div>
            <div class="security-item"><div class="dot dot-green"></div><div class="security-label">SonarQube SAST Scan</div><span class="badge badge-green">0 Critical</span></div>
            <div class="security-item"><div class="dot dot-green"></div><div class="security-label">Trivy Image Scan</div><span class="badge badge-green">0 HIGH/CRITICAL</span></div>
            <div class="security-item"><div class="dot dot-green"></div><div class="security-label">K8s Network Policies</div><span class="badge badge-green">Applied</span></div>
            <div class="security-item"><div class="dot dot-green"></div><div class="security-label">AWS Secrets Manager</div><span class="badge badge-green">Active</span></div>
            <div class="security-item"><div class="dot dot-green"></div><div class="security-label">RBAC Policies</div><span class="badge badge-green">Enforced</span></div>
            <div class="security-item"><div class="dot dot-yellow"></div><div class="security-label">SSL Certificate</div><span class="badge badge-yellow">Renew in 30d</span></div>
        </div>

    </div>

    <!-- Audit Log -->
    <div class="section">
        <h2>Recent Audit Log</h2>
        <table>
            <tr>
                <th>Timestamp</th>
                <th>User</th>
                <th>Action</th>
                <th>Resource</th>
                <th>Status</th>
            </tr>
            <tr><td>2026-05-05 09:12</td><td>dr.admin</td><td>VIEW</td><td>Patient P-1042 Records</td><td><span class="badge badge-green">Allowed</span></td></tr>
            <tr><td>2026-05-05 09:08</td><td>jenkins-ci</td><td>DEPLOY</td><td>healthcare-app:v42</td><td><span class="badge badge-blue">Success</span></td></tr>
            <tr><td>2026-05-05 09:05</td><td>jenkins-ci</td><td>SCAN</td><td>Trivy Image Scan</td><td><span class="badge badge-green">Passed</span></td></tr>
            <tr><td>2026-05-05 08:55</td><td>unknown</td><td>LOGIN</td><td>Admin Portal</td><td><span class="badge badge-red">Blocked</span></td></tr>
            <tr><td>2026-05-05 08:42</td><td>nurse.priya</td><td>UPDATE</td><td>Patient P-1039 vitals</td><td><span class="badge badge-green">Allowed</span></td></tr>
        </table>
    </div>

    <div class="alert-box">
        ⚠ Security Alert: 1 unauthorized login attempt blocked at 08:55. IP has been flagged and reported to security team.
    </div>

</div>

<div class="footer">SecureHealth v1.0 — DevSecOps Enabled — HIPAA Compliant — Deployed via Jenkins CI/CD on AWS</div>

</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
