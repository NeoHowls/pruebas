//Obtener roles de usuario
const listProfiles = async () => {
    try {
        const response = await fetch("../profiles/");
        const data = await response.json();
        
        if(data.message == "Success") {
            let options = ``;
                options += `<option value='0'>Rol de usuario</option>`;
            data.profiles.forEach((profile)=>{
                options += `<option value='${profile.id}'>${profile.name}</option>`;
            })
            selectProfile.innerHTML=options;
        }
        else {
            selectProfile.innerHTML=``;
        }
    }
    catch(error) {
        console.log(error);
    }

    selectProfile.addEventListener("change", (event) => {
        const value = event.target.value;
        if(value == 0) {
            checkSelectProfile.classList.replace("checkIcon", "checkIconHidden")
        }
        else {
            checkSelectProfile.classList.replace("checkIconHidden", "checkIcon")
        }
        listStations(value);
    })
}


//Obtener lista de ciudades
const listStations = async (id) => {
    if(id == 0) {
        selectStation.innerHTML=``;
    }
    else {
        try {
            const response = await fetch(`../stations/${id}`);
            const data = await response.json();
            
            if(data.message == "Success") {
                let options = ``;
                    options += `<option value=0>Seleccionar estación</option>`;
                data.stations.forEach((station)=>{
                    options += `<option value=${station.id}>${station.name}</option>`;
                })
                selectStation.innerHTML=options;
            }
            else {
                selectStation.innerHTML=``;
            }
        }
        catch(error) {
            console.log(error);
        }
    }

    selectStation.addEventListener("change", (event) => {
        const value = event.target.value;
        if(value == 0) {
            checkSelectStation.classList.replace("checkIcon", "checkIconHidden")
        }
        else {
            checkSelectStation.classList.replace("checkIconHidden", "checkIcon")
        }
    })
}

//Obtener lista de ciudades
const listComunes = async (id) => {
    if(id == 0) {
        selectComune.innerHTML=``;
    }
    else {
        try {
            const response = await fetch(`../comunes/${id}`);
            const data = await response.json();
            
            if(data.message == "Success") {
                let options = ``;
                    options += `<option value=0>Seleccionar comuna</option>`;
                data.comunes.forEach((comune)=>{
                    options += `<option value=${comune.id}>${comune.name}</option>`;
                })
                selectComune.innerHTML=options;
            }
            else {
                selectComune.innerHTML=``;
            }
        }
        catch(error) {
            console.log(error);
        }
    }

    selectComune.addEventListener("change", (event) => {
        const value = event.target.value;
        if(value == 0) {
            checkSelectComune.classList.replace("checkIcon", "checkIconHidden")
        }
        else {
            checkSelectComune.classList.replace("checkIconHidden", "checkIcon")
        }
        listStations(value);
    })
}

//Obtener lista de regiones
const listRegions = async() => {
    try {
        const response = await fetch("../regions/");
        const data = await response.json();
        
        if(data.message == "Success") {
            let options = ``;
                options += `<option value=0>Seleccionar región</option>`;
            data.regions.forEach((region)=>{
                options += `<option value="${region.id}">${region.name}</option>`;
            })
            selectRegion.innerHTML=options;
        }
        else {
            selectRegion.innerHTML=``;
        }
    }
    catch(error) {
        console.log(error);
    }
};

//Carga inicial - Sólo carga el listado de regiones
const startLoad = async () => {
    await listRegions();
    await listProfiles();

    selectRegion.addEventListener("change", (event) => {
        const value = event.target.value;
        if(value == 0) {
            checkSelectRegion.classList.replace("checkIcon", "checkIconHidden")
        }
        else {
            checkSelectRegion.classList.replace("checkIconHidden", "checkIcon")
        }
        listComunes(value);
    });
};

//Evento load cuando se cargue el DOM
window.addEventListener("load", async () => {
    await startLoad();
});