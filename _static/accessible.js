/* HTML tweaks to address accessibility concerns noted in audit by Allia Service at U Oregon */

function add_aria_labels() {
    /* Full-screen toggle button lacks an Aria label as of August 2023 */
    const fullscreen_toggle = document.querySelector(".btn-fullscreen-button");
    fullscreen_toggle.setAttribute("aria-label", "Full screen toggle");
    /* Code region copy buttons need ARIA labels */

}

add_aria_labels();