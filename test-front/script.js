document.getElementById("sendBtn").addEventListener("click", () => {
    // window.API_URL은 index.html에서 런타임에 설정됨
    fetch(`${window.API_URL}/api/send`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: "Send" }),
    })
        .then((resp) => resp.json()) // Fetch API 사용 예 :contentReference[oaicite:4]{index=4}
        .then((data) => {
            if (data.response === "Received") {
                console.log("Received");
            }
        })
        .catch((err) => console.error("Error:", err));
});
