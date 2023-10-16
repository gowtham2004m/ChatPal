$(document).ready(function () {
    $('#send-button').click(function () {
        sendMessage();
    });

    $('#user-input').keypress(function (e) {
        if (e.which === 13) {
            sendMessage();
        }
    });

    function sendMessage() {
        var userMessage = $('#user-input').val();
        if (userMessage.trim() === "") return;

        appendMessage('You', userMessage);

        // Send user's message to the chatbot and get a response
        $.post('/chatbot', { message: userMessage }, function (response) {
            appendMessage('Bot', response.response);
        });

        $('#user-input').val('');
    }

    function appendMessage(sender, message) {
        var chatbox = $('#chat');
        chatbox.append('<p><strong>' + sender + ':</strong> ' + message + '</p>');
        chatbox.scrollTop(chatbox[0].scrollHeight);
    }
});
