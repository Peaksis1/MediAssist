async function handleSubmit(event) {
    event.preventDefault(); // Prevents default form submission

    // Get form data
    const formData = new FormData(event.target);
    const data = {
        name: formData.get("name"),
        email: formData.get("email"),
        message: formData.get("message"),
    };

    try {
        // Send the form data to the backend using fetch
        const response = await fetch("http://127.0.0.1:5000/send-email", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });

        // Handle response from backend
        if (response.ok) {
            alert("Message sent successfully!");
        } else {
            alert("Failed to send message.");
        }
    } catch (error) {
        alert("Error sending message. Please try again later.");
    }
}