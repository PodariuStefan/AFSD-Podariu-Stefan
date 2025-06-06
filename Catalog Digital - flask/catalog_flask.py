from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'catalog_secret_key_2024'

# Configurare pentru template-uri și fișiere statice
app.template_folder = 'templates'
app.static_folder = 'static'

# Fișierul pentru stocarea datelor
DATA_FILE = 'catalog_data.json'

def load_students():
    """Încarcă studenții din fișierul JSON"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []

def save_students(students):
    """Salvează studenții în fișierul JSON"""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(students, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Eroare la salvarea datelor: {e}")
        return False

def get_next_id():
    """Generează următorul ID disponibil"""
    students = load_students()
    if not students:
        return 1
    return max(student.get('id', 0) for student in students) + 1

@app.route('/')
def index():
    """Pagina principală - afișează lista de studenți"""
    students = load_students()
    return render_template('index.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    """Adaugă un student nou"""
    if request.method == 'POST':
        # Obține datele din formular
        nume = request.form.get('nume', '').strip()
        prenume = request.form.get('prenume', '').strip()
        nota = request.form.get('nota', '').strip()
        materie = request.form.get('materie', '').strip()
        
        # Validare date
        if not all([nume, prenume, nota, materie]):
            flash('Toate câmpurile sunt obligatorii!', 'error')
            return render_template('add_student.html')
        
        try:
            nota_float = float(nota)
            if not (1 <= nota_float <= 10):
                flash('Nota trebuie să fie între 1 și 10!', 'error')
                return render_template('add_student.html')
        except ValueError:
            flash('Nota trebuie să fie un număr valid!', 'error')
            return render_template('add_student.html')
        
        # Creează obiectul student
        student = {
            'id': get_next_id(),
            'nume': nume,
            'prenume': prenume,
            'nota': round(nota_float, 2),
            'materie': materie,
            'data_adaugare': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Salvează studentul
        students = load_students()
        students.append(student)
        
        if save_students(students):
            flash(f'Studentul {nume} {prenume} a fost adăugat cu succes!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Eroare la salvarea datelor!', 'error')
    
    return render_template('add_student.html')

@app.route('/edit_student/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    """Editează un student existent"""
    students = load_students()
    student = next((s for s in students if s['id'] == student_id), None)
    
    if not student:
        flash('Studentul nu a fost găsit!', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        # Obține datele din formular
        nume = request.form.get('nume', '').strip()
        prenume = request.form.get('prenume', '').strip()
        nota = request.form.get('nota', '').strip()
        materie = request.form.get('materie', '').strip()
        
        # Validare date
        if not all([nume, prenume, nota, materie]):
            flash('Toate câmpurile sunt obligatorii!', 'error')
            return render_template('edit_student.html', student=student)
        
        try:
            nota_float = float(nota)
            if not (1 <= nota_float <= 10):
                flash('Nota trebuie să fie între 1 și 10!', 'error')
                return render_template('edit_student.html', student=student)
        except ValueError:
            flash('Nota trebuie să fie un număr valid!', 'error')
            return render_template('edit_student.html', student=student)
        
        # Actualizează datele studentului
        student.update({
            'nume': nume,
            'prenume': prenume,
            'nota': round(nota_float, 2),
            'materie': materie,
            'data_modificare': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
        if save_students(students):
            flash(f'Datele pentru {nume} {prenume} au fost actualizate!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Eroare la salvarea datelor!', 'error')
    
    return render_template('edit_student.html', student=student)

@app.route('/delete_student/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    """Șterge un student"""
    students = load_students()
    student = next((s for s in students if s['id'] == student_id), None)
    
    if not student:
        flash('Studentul nu a fost găsit!', 'error')
        return redirect(url_for('index'))
    
    # Șterge studentul din listă
    students = [s for s in students if s['id'] != student_id]
    
    if save_students(students):
        flash(f'Studentul {student["nume"]} {student["prenume"]} a fost șters!', 'success')
    else:
        flash('Eroare la ștergerea studentului!', 'error')
    
    return redirect(url_for('index'))

@app.route('/view_student/<int:student_id>')
def view_student(student_id):
    """Afișează detaliile unui student"""
    students = load_students()
    student = next((s for s in students if s['id'] == student_id), None)
    
    if not student:
        flash('Studentul nu a fost găsit!', 'error')
        return redirect(url_for('index'))
    
    return render_template('view_student.html', student=student)

@app.route('/api/students')
def api_students():
    """API endpoint pentru obținerea listei de studenți"""
    students = load_students()
    return jsonify(students)

@app.route('/api/student/<int:student_id>')
def api_student(student_id):
    """API endpoint pentru obținerea unui student specific"""
    students = load_students()
    student = next((s for s in students if s['id'] == student_id), None)
    
    if student:
        return jsonify(student)
    else:
        return jsonify({'error': 'Student not found'}), 404

if __name__ == '__main__':
    # Creează directoarele necesare dacă nu există
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5000)