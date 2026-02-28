@app.route('/compound-interest', methods=['GET', 'POST'])
def compound_interest():
    result = None
    dias_mes = None

    if request.method == "POST":
        try:
            capital = float(request.form["capital"])
            tasa = float(request.form["tasa"])
            mes = int(request.form["mes"])
            anio = int(request.form["anio"])

            dias_mes = calendar.monthrange(anio, mes)[1]

            # Convertimos tasa anual a diaria
            tasa_diaria = tasa / 100 / 365

            rendimiento_diario = capital * tasa_diaria
            rendimiento_mensual = rendimiento_diario * dias_mes
            rendimiento_anual = capital * (tasa / 100)

            result = {
                "diario": round(rendimiento_diario, 2),
                "mensual": round(rendimiento_mensual, 2),
                "anual": round(rendimiento_anual, 2),
                "dias_mes": dias_mes
            }

        except:
            result = "Invalid input"

    return render_template('compound_interest.html', result=result)
