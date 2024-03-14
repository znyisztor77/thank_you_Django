console.log('Ez csak egy gyakorló szöveg')


// tankolási adataok
const refuelsEl = document.querySelector('#refuels')
fetch('/api/refuels/')
.then(res => res.json())
.then(data => {
        data.forEach(refuel => {

            wrapper = document.createElement('div')

            element = document.createElement('h3')
            element.innerText = refuel.distance_km 
            wrapper.appendChild(element)

            petrol = document.createElement('h4')
            petrol.innerText = refuel.petrol_amount_liter + "liter"
            wrapper.appendChild(petrol)

            date = document.createElement('h4')
            date.innerText = refuel.refuel_date            
            wrapper.appendChild(date)
            
            refuelsEl.appendChild(wrapper)
            
        });
})

fetch('/api/consuption/')
.then(res => res.json())
.then(data => {
        let cons = document.getElementById('consuption')
        cons.innerText = data.consuption
})