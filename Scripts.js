async function yuborish() {
    let savol = document.getElementById('inputBox').value;

    // Python-ga (Backend) ma'lumot yuborish
    let response = await fetch('/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ savol: savol })
    });

    let natija = await response.json();
    
    // Python-dan kelgan javobni ekranga chiqarish
    document.getElementById('display').innerText = natija.javob;
}