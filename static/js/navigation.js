document.addEventListener("DOMContentLoaded", function () {
    const container = document.querySelector(".slide-container");
    if (!container) return;

    const prevUrl = container.dataset.prev;
    const nextUrl = container.dataset.next;
    const firstUrl = container.dataset.first;

    document.addEventListener("keydown", function (e) {
        // Don't navigate if user is typing in an input
        if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;

        switch (e.key) {
            case "ArrowRight":
            case "ArrowDown":
                if (nextUrl) window.location.href = nextUrl;
                break;
            case "ArrowLeft":
            case "ArrowUp":
                if (prevUrl) window.location.href = prevUrl;
                break;
            case "Home":
                if (firstUrl) window.location.href = firstUrl;
                e.preventDefault();
                break;
        }
    });
});
