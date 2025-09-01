// Scene
const scene = new THREE.Scene();

// Camera
const camera = new THREE.PerspectiveCamera(
  75, 
  window.innerWidth / window.innerHeight, 
  0.1, 
  1000
);
camera.position.z = 3;

// Renderer
const renderer = new THREE.WebGLRenderer({
  antialias: true,
  alpha: true});

renderer.setSize(400, 200);
camera.aspect = 1
document.getElementById('globe-container').appendChild(renderer.domElement);

// Sphere geometry (globe)
const geometry = new THREE.SphereGeometry(1, 64, 64);

// Material (basic color for now, can replace with Earth texture)
const material = new THREE.MeshStandardMaterial({
  color: 0xffffff,
  roughness: 0.7,
  metalness: 0.0,
});

const sphere = new THREE.Mesh(geometry, material);
scene.add(sphere);

// Lighting
const light = new THREE.PointLight(0xffffff, 1);
light.position.set(5, 5, 5);
scene.add(light);

const ambientLight = new THREE.AmbientLight(0x404040); // soft light
scene.add(ambientLight);

// Animation loop
function animate() {
  requestAnimationFrame(animate);

  // Rotate sphere
  sphere.rotation.y += 0.01;

  renderer.render(scene, camera);
}
animate();

// Handle resizing
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

document.getElementById('globe-display').innerHTML = 
  '<div class="loading">LOADING GLOBE...</div>';
