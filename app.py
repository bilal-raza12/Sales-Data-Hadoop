from flask import Flask, render_template_string
import os

app = Flask(__name__)

def get_results():
    data = {}
    with open('/home/bilal-raza/sales_project/results.txt', 'r') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                data[parts[0]] = float(parts[1])
    return data

@app.route('/')
def index():
    data = get_results()
    labels = list(data.keys())
    values = list(data.values())
    
    html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Sales Analysis Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: Arial, sans-serif; 
            background: #1a1a2e; 
            color: white; 
            padding: 20px;
        }
        h1 { 
            text-align: center; 
            color: #00d4ff; 
            margin-bottom: 10px;
            font-size: 2em;
        }
        p.subtitle {
            text-align: center;
            color: #888;
            margin-bottom: 30px;
        }
        .charts-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 30px;
        }
        .chart-box {
            background: #16213e;
            border-radius: 15px;
            padding: 20px;
            width: 500px;
            box-shadow: 0 4px 20px rgba(0,212,255,0.2);
        }
        .chart-box h2 {
            text-align: center;
            color: #00d4ff;
            margin-bottom: 15px;
        }
        .stats {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }
        .stat-card {
            background: #16213e;
            border-radius: 10px;
            padding: 15px 25px;
            text-align: center;
            border: 1px solid #00d4ff;
        }
        .stat-card h3 { color: #00d4ff; font-size: 1.5em; }
        .stat-card p { color: #888; font-size: 0.9em; }
    </style>
</head>
<body>
    <h1>📊 Sales Data Analysis</h1>
    <p class="subtitle">Powered by Hadoop MapReduce</p>
    
    <div class="stats">
        <div class="stat-card">
            <h3>''' + str(len(labels)) + '''</h3>
            <p>Product Lines</p>
        </div>
        <div class="stat-card">
            <h3>$''' + str(round(sum(values), 1)) + '''</h3>
            <p>Total Sales</p>
        </div>
        <div class="stat-card">
            <h3>''' + max(data, key=data.get) + '''</h3>
            <p>Top Product</p>
        </div>
    </div>

    <div class="charts-container">
        <div class="chart-box">
            <h2>📊 Sales by Product Line (Bar)</h2>
            <canvas id="barChart"></canvas>
        </div>
        <div class="chart-box">
            <h2>🥧 Sales Distribution (Pie)</h2>
            <canvas id="pieChart"></canvas>
        </div>
    </div>

    <script>
        const labels = ''' + str(labels) + ''';
        const values = ''' + str(values) + ''';
        const colors = ['#00d4ff','#ff6b6b','#ffd93d','#6bcb77','#4d96ff','#ff6bff','#ff9f43'];

        new Chart(document.getElementById('barChart'), {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Total Sales ($)',
                    data: values,
                    backgroundColor: colors,
                    borderRadius: 8
                }]
            },
            options: {
                plugins: { legend: { labels: { color: 'white' }}},
                scales: {
                    x: { ticks: { color: 'white' }, grid: { color: '#333' }},
                    y: { ticks: { color: 'white' }, grid: { color: '#333' }}
                }
            }
        });

        new Chart(document.getElementById('pieChart'), {
            type: 'doughnut',
            data: {
                labels: labels,
                datasets: [{
                    data: values,
                    backgroundColor: colors
                }]
            },
            options: {
                plugins: { legend: { labels: { color: 'white' }}}
            }
        });
    </script>
</body>
</html>
    '''
    return html

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
