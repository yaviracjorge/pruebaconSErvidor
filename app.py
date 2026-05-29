from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hola Mundo Flask</title>

    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family: Arial, Helvetica, sans-serif;
        }

        body{
            height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            background: linear-gradient(135deg, #4facfe, #00f2fe);
        }

        .card{
            background:white;
            padding:50px;
            border-radius:20px;
            text-align:center;
            box-shadow:0 10px 30px rgba(0,0,0,0.2);
            width:400px;
            animation: fadeIn 1s ease;
        }

        h1{
            font-size:48px;
            color:#333;
            margin-bottom:15px;
        }

        p{
            color:#666;
            font-size:18px;
            margin-bottom:25px;
        }

        .btn{
            display:inline-block;
            padding:12px 25px;
            border-radius:10px;
            text-decoration:none;
            background:#4facfe;
            color:white;
            font-weight:bold;
            transition:0.3s;
        }

        .btn:hover{
            background:#0077ff;
            transform:scale(1.05);
        }

        @keyframes fadeIn{
            from{
                opacity:0;
                transform:translateY(20px);
            }
            to{
                opacity:1;
                transform:translateY(0);
            }
        }
    </style>
</head>

<body>

    <div class="card">
        <h1>👋 Hola Mundo</h1>
        <p>Mi primera aplicación con Flask y Python</p>
        <a class="btn" href="/">Recargar</a>
    </div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)

