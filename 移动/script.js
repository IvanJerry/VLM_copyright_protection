document.addEventListener('DOMContentLoaded', function() {
    // Tab切换
    const tabBtns = document.querySelectorAll('.tab-btn');
    const pages = {
        chat: document.getElementById('page-chat'),
        model: document.getElementById('page-model'),
        watermark: document.getElementById('page-watermark'),
        settings: document.getElementById('page-settings')
    };
    tabBtns.forEach(btn => {
        btn.onclick = function() {
            tabBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            Object.values(pages).forEach(p => p.style.display = 'none');
            pages[btn.dataset.tab].style.display = 'block';
        };
    });

    // 聊天功能
    const chatHistory = document.getElementById('chat-history');
    const chatInput = document.getElementById('chat-input');
    const sendBtn = document.getElementById('send-btn');

    function appendUserMsg(text) {
        const row = document.createElement('div');
        row.className = 'mobile-chat-row user';
        const bubble = document.createElement('div');
        bubble.className = 'mobile-chat-bubble user';
        bubble.textContent = text;
        row.appendChild(bubble);
        chatHistory.appendChild(row);
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }

    sendBtn.onclick = function() {
        const val = chatInput.value.trim();
        if (!val) return;
        appendUserMsg(val);
        chatInput.value = '';
    };

    chatInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') sendBtn.onclick();
    });
}); 