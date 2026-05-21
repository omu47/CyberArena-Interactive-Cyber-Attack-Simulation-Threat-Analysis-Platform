const messages = document.querySelectorAll(".bot-message");

messages.forEach((msg, index) => {

    msg.style.opacity = "0";

    setTimeout(() => {

        msg.style.opacity = "1";

        msg.style.transition = "1s";

    }, index * 1000);

});