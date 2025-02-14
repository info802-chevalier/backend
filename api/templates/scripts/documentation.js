class DocumentationService {
  constructor(documentation) {
    this.documentation = documentation;
  }
  getDocumentation() {
    return this.documentation;
  }

  renderEndpoint(endpoint) {
    // -- DOM ELEMENTS --
    const endpointsDiv = document.getElementById("documentation");
    const endpointDiv = document.createElement("div");

    endpointDiv.innerHTML = `
            <h2> <span class="method ${endpoint.operations[0].method}">${endpoint.operations[0].method}</span> - <span class="path">${endpoint.path}</span></h2>
            <p class="summary">${endpoint.operations[0].summary}</p>
            <p class="notes">${endpoint.operations[0].notes}</p>
          `;

    endpoint.operations[0].parameters.forEach((parameter) => {
      endpointDiv.innerHTML += `
                <p class="parameter"><span class="name">${parameter.name}</span> - <span class="type">${parameter.dataType}</span></p>
              `;
    });

    endpointDiv.classList.add("endpoint");
    endpointsDiv.appendChild(endpointDiv);
  }

  render() {
    // -- DOM ELEMENTS --
    const apiPath = document.getElementById("api-path");
    const apiDescription = document.getElementById("api-description");

    const documentation = this.getDocumentation();

    apiPath.textContent = documentation.basePath + "/api";
    apiDescription.textContent = documentation.description;

    documentation.apis.forEach((endpoint) => {
      this.renderEndpoint(endpoint);
    });
  }
}

const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
    "Access-Control-Allow-Headers": "Content-Type",
  },
});

const API_URL = "https://backend-tau-plum.vercel.app";

const Documentation = async function () {
  return api.get(`/documentation`);
};

const documentation = await Documentation();
const documentationService = new DocumentationService(documentation.data);
console.log(documentationService.getDocumentation());
documentationService.render();
