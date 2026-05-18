async function generateCareerGuidance() {

    const skills =
        document.getElementById('skills').value;

    const interests =
        document.getElementById('interests').value;

    const experience =
        document.getElementById('experience').value;

    const goals =
        document.getElementById('goals').value;

    const resultDiv =
        document.getElementById('result');


    resultDiv.innerHTML = `
    
        <div class="loading">
            Generating AI career roadmap...
        </div>
    
    `;


    const response = await fetch('/generate', {

        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({
            skills,
            interests,
            experience,
            goals
        })

    });


    const data = await response.json();


    // CONVERT MARKDOWN TO HTML

    resultDiv.innerHTML = marked.parse(data.response);

}