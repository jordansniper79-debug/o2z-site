document.addEventListener('DOMContentLoaded', () => {

    // Center node logic interactions
    const centerNode = document.querySelector('.center-node');
    
    // Simulate data ping across network visually
    setInterval(() => {
        centerNode.style.boxShadow = '0 0 60px rgba(0, 240, 255, 0.4), inset 0 0 20px rgba(0, 240, 255, 0.3)';
        setTimeout(() => {
            centerNode.style.boxShadow = '';
        }, 800);
    }, 4500);

    // Live Stream Logs generator (Simulating the intelligence routing System)
    const logsBody = document.getElementById('live-logs');
    const logMessages = [
        { msg: "Omni-Ingestion: Incoming WhatsApp message detected.", status: "routing", type: "system" },
        { msg: "AI Sentiment Analysis: Intent -> Pricing Query, Industry -> Real Estate.", status: "success", type: "ai" },
        { msg: "The Automation Core: Triggering n8n Workflow 'Lead-to-Client'.", status: "routing", type: "automation" },
        { msg: "Stitch UI Sync: Real-time UI data update pushed.", status: "success", type: "ui" },
        { msg: "Intelligence Layer: Updating Master Profile (CDP) for User [ID: 9481].", status: "success", type: "cdp" },
        { msg: "Growth Engine: CPA monitored - Stable conversion rate.", status: "success", type: "growth" }
    ];

    let messageIndex = 0;

    function addLogEntry() {
        if(logsBody.children.length >= 6) {
            logsBody.removeChild(logsBody.firstElementChild); // keep recent
        }

        const logData = logMessages[messageIndex];
        const now = new Date();
        const timeString = `${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}:${now.getSeconds().toString().padStart(2, '0')}`;

        const div = document.createElement('div');
        div.className = 'log-entry';
        
        div.innerHTML = `
            <span class="log-time">[${timeString}]</span>
            <span class="log-status ${logData.status}">[${logData.type.toUpperCase()}]</span>
            <span class="log-message">${logData.msg}</span>
        `;
        
        logsBody.appendChild(div);

        // Flash an element on the screen representing this activity
        const uiElementToFlash = document.querySelector(`[data-pulse-target="${logData.type}"]`);
        if(uiElementToFlash) {
            uiElementToFlash.classList.add('flash-active');
            setTimeout(() => uiElementToFlash.classList.remove('flash-active'), 500);
        }

        messageIndex = (messageIndex + 1) % logMessages.length;
        
        // Randomize next log time
        setTimeout(addLogEntry, Math.random() * 2000 + 1500);
    }

    addLogEntry();
});
