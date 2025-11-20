import React, { useState } from "react";

// LoginGreen.jsx
// Usage: place <LoginGreen /> anywhere in your React app. Requires Tailwind CSS

export default function LoginGreen() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState("");

  function handleSubmit(e) {
    e.preventDefault();
    setError("");
    // Simple client-side validation (replace with real auth)
    if (!email) return setError("Veuillez saisir votre email.");
    if (!password) return setError("Veuillez saisir votre mot de passe.");
    // mock success
    alert(`Connexion réussie pour ${email}`);
  }

  return (
    <div className="min-h-screen bg-gradient-to-b from-green-50 to-white flex flex-col">
      {/* Top content area (the "framework") */}
      <header className="p-6">
        <h1 className="text-2xl font-semibold text-green-800">Mon Application</h1>
        <p className="text-sm text-green-600/80">Interface de connexion — style vert élégant</p>
      </header>

      {/* Filler so the login sits near the bottom of the layout */}
      <main className="flex-1"></main>

      {/* The "table connexion" centered at the bottom */}
      <footer className="w-full flex justify-center items-end pb-12">
        <form
          onSubmit={handleSubmit}
          className="w-full max-w-md bg-white/90 backdrop-blur-md border border-green-100 shadow-xl rounded-2xl px-8 py-6 mx-4 transform transition-all duration-300 hover:scale-[1.01]"
          aria-label="Formulaire de connexion"
        >
          <div className="flex items-center gap-3 mb-4">
            <div className="flex-none w-12 h-12 rounded-full bg-gradient-to-br from-green-400 to-green-600 flex items-center justify-center shadow-md">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M16 11V7a4 4 0 00-8 0v4M5 11h14l1 9H4l1-9z" />
              </svg>
            </div>
            <div>
              <h2 className="text-lg font-semibold text-green-800">Connexion</h2>
              <p className="text-xs text-green-600/80">Entrez votre email et mot de passe</p>
            </div>
          </div>

          {error && <div className="text-sm text-red-600 mb-3">{error}</div>}

          <label className="block text-sm text-green-700">Email</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="vous@exemple.com"
            className="w-full mt-1 mb-4 px-4 py-2 rounded-lg border border-green-100 focus:outline-none focus:ring-2 focus:ring-green-300 focus:border-transparent"
            required
            aria-required
          />

          <label className="block text-sm text-green-700">Mot de passe</label>
          <div className="relative">
            <input
              type={showPassword ? "text" : "password"}
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="••••••••"
              className="w-full mt-1 mb-4 px-4 py-2 rounded-lg border border-green-100 focus:outline-none focus:ring-2 focus:ring-green-300 focus:border-transparent"
              required
            />
            <button
              type="button"
              onClick={() => setShowPassword((s) => !s)}
              className="absolute right-2 top-1/2 -translate-y-1/2 text-sm px-2 py-1 rounded-md text-green-700 hover:bg-green-50"
              aria-label={showPassword ? "Masquer le mot de passe" : "Afficher le mot de passe"}
            >
              {showPassword ? "Cacher" : "Afficher"}
            </button>
          </div>

          <div className="flex items-center justify-between mb-4">
            <label className="flex items-center gap-2 text-sm text-green-700">
              <input type="checkbox" className="w-4 h-4 rounded border-green-200" />
              Se souvenir de moi
            </label>
            <a href="#" className="text-sm text-green-600 hover:underline">Mot de passe oublié ?</a>
          </div>

          <button
            type="submit"
            className="w-full py-2 rounded-xl bg-gradient-to-r from-green-500 to-green-600 text-white font-semibold shadow-md hover:shadow-lg active:scale-[0.995] transition-all"
          >
            Connexion
          </button>

          <p className="text-center text-xs text-green-600/70 mt-3">En vous connectant, vous acceptez nos conditions.</p>
        </form>
      </footer>
    </div>
  );
}













