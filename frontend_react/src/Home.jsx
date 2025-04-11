import React from "react"

import "./Home.css"

const Home = () => {
    return (
        <div id="webcrumbs">
            <div className="bg-white min-h-screen p-6 lg:min-w-[1000px]">
                <header className="flex justify-between items-center mb-6">
                    <h1 className="text-2xl font-bold text-gray-800">Painel de Logística</h1>
                    <div className="flex items-center text-gray-600">
                        <span>Bem-vindo, Admin</span>
                        <span className="material-symbols-outlined ml-2 bg-primary-500 text-white rounded-full p-1 cursor-pointer hover:bg-primary-600 transition-colors">
                            person
                        </span>
                    </div>
                </header>

                <section className="bg-white rounded-lg shadow-sm p-6 mb-6">
                    <h2 className="text-lg font-semibold text-gray-800 mb-4">Status das Entregas</h2>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div className="flex border-l-4 border-green-500 bg-green-50 p-4 rounded-r-lg">
                            <div className="flex-shrink-0 mr-4">
                                <span className="flex items-center justify-center w-10 h-10 bg-green-100 text-green-500 rounded-full">
                                    <span className="material-symbols-outlined">check_circle</span>
                                </span>
                            </div>
                            <div>
                                <h3 className="font-bold text-3xl text-gray-800">185</h3>
                                <div className="flex items-center">
                                    <span className="text-sm text-green-600 font-medium">(+12.8%)</span>
                                    <span className="text-xs text-gray-500 ml-2">Comparado ao mês anterior</span>
                                </div>
                                <p className="text-sm text-gray-600 mt-1">Entregas no Prazo</p>
                            </div>
                        </div>

                        <div className="flex border-l-4 border-red-500 bg-red-50 p-4 rounded-r-lg">
                            <div className="flex-shrink-0 mr-4">
                                <span className="flex items-center justify-center w-10 h-10 bg-red-100 text-red-500 rounded-full">
                                    <span className="material-symbols-outlined">warning</span>
                                </span>
                            </div>
                            <div>
                                <h3 className="font-bold text-3xl text-gray-800">23</h3>
                                <div className="flex items-center">
                                    <span className="text-xs text-gray-500">Necessitam atenção imediata</span>
                                </div>
                                <p className="text-sm text-gray-600 mt-1">Entregas Atrasadas</p>
                            </div>
                        </div>
                    </div>
                </section>

                <section className="bg-white rounded-lg shadow-sm p-6 mb-6">
                    <h2 className="text-lg font-semibold text-gray-800 mb-4">Entregas do Dia</h2>
                    <div className="overflow-x-auto">
                        <table className="min-w-full divide-y divide-gray-200">
                            <thead>
                                <tr className="text-left text-gray-500 text-sm">
                                    <th className="py-3 px-4">ID do Pedido</th>
                                    <th className="py-3 px-4">Cidade</th>
                                    <th className="py-3 px-4">Ações</th>
                                </tr>
                            </thead>
                            <tbody className="divide-y divide-gray-100">
                                <tr className="hover:bg-gray-50 transition-colors">
                                    <td className="py-3 px-4 text-blue-600 font-medium">#ORD-2350</td>
                                    <td className="py-3 px-4">Curitiba, PR</td>
                                    <td className="py-3 px-4">
                                        <button className="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-sm transition-colors">
                                            Detalhes
                                        </button>
                                    </td>
                                </tr>
                                <tr className="hover:bg-gray-50 transition-colors">
                                    <td className="py-3 px-4 text-blue-600 font-medium">#ORD-2351</td>
                                    <td className="py-3 px-4">Porto Alegre, RS</td>
                                    <td className="py-3 px-4">
                                        <button className="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-sm transition-colors">
                                            Detalhes
                                        </button>
                                    </td>
                                </tr>
                                <tr className="hover:bg-gray-50 transition-colors">
                                    <td className="py-3 px-4 text-blue-600 font-medium">#ORD-2352</td>
                                    <td className="py-3 px-4">Goiânia, GO</td>
                                    <td className="py-3 px-4">
                                        <button className="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-sm transition-colors">
                                            Detalhes
                                        </button>
                                    </td>
                                </tr>
                                <tr className="hover:bg-gray-50 transition-colors">
                                    <td className="py-3 px-4 text-blue-600 font-medium">#ORD-2353</td>
                                    <td className="py-3 px-4">Manaus, AM</td>
                                    <td className="py-3 px-4">
                                        <button className="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-sm transition-colors">
                                            Detalhes
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>

                <section className="bg-white rounded-lg shadow-sm p-6">
                    <h2 className="text-lg font-semibold text-gray-800 mb-4">Entregas Pendentes</h2>
                    <div className="overflow-x-auto">
                        <table className="min-w-full divide-y divide-gray-200">
                            <thead>
                                <tr className="text-left text-gray-500 text-sm">
                                    <th className="py-3 px-4">ID do Pedido</th>
                                    <th className="py-3 px-4">Cidade</th>
                                    <th className="py-3 px-4">Data Prevista</th>
                                    <th className="py-3 px-4">Status</th>
                                    <th className="py-3 px-4">Ações</th>
                                </tr>
                            </thead>
                            <tbody className="divide-y divide-gray-100">
                                <tr className="hover:bg-gray-50 transition-colors">
                                    <td className="py-3 px-4 text-blue-600 font-medium">#ORD-2345</td>
                                    <td className="py-3 px-4">São Paulo, SP</td>
                                    <td className="py-3 px-4">16/07/2024</td>
                                    <td className="py-3 px-4">
                                        <span className="px-2 py-1 bg-yellow-100 text-yellow-800 rounded-full text-xs">
                                            Atrasada
                                        </span>
                                    </td>
                                    <td className="py-3 px-4">
                                        <button className="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-sm transition-colors">
                                            Detalhes
                                        </button>
                                    </td>
                                </tr>
                                <tr className="bg-yellow-50 hover:bg-yellow-100 transition-colors">
                                    <td className="py-3 px-4 text-blue-600 font-medium">#ORD-2346</td>
                                    <td className="py-3 px-4">Rio de Janeiro, RJ</td>
                                    <td className="py-3 px-4">17/07/2024</td>
                                    <td className="py-3 px-4">
                                        <span className="px-2 py-1 bg-yellow-100 text-yellow-800 rounded-full text-xs">
                                            Atrasada
                                        </span>
                                    </td>
                                    <td className="py-3 px-4">
                                        <button className="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-sm transition-colors">
                                            Detalhes
                                        </button>
                                    </td>
                                </tr>
                                <tr className="hover:bg-gray-50 transition-colors">
                                    <td className="py-3 px-4 text-blue-600 font-medium">#ORD-2347</td>
                                    <td className="py-3 px-4">Belo Horizonte, MG</td>
                                    <td className="py-3 px-4">15/07/2024</td>
                                    <td className="py-3 px-4">
                                        <span className="px-2 py-1 bg-gray-100 text-gray-800 rounded-full text-xs">
                                            No prazo
                                        </span>
                                    </td>
                                    <td className="py-3 px-4">
                                        <button className="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-sm transition-colors">
                                            Detalhes
                                        </button>
                                    </td>
                                </tr>
                                <tr className="hover:bg-gray-50 transition-colors">
                                    <td className="py-3 px-4 text-blue-600 font-medium">#ORD-2348</td>
                                    <td className="py-3 px-4">Salvador, BA</td>
                                    <td className="py-3 px-4">16/07/2024</td>
                                    <td className="py-3 px-4">
                                        <span className="px-2 py-1 bg-gray-100 text-gray-800 rounded-full text-xs">
                                            No prazo
                                        </span>
                                    </td>
                                    <td className="py-3 px-4">
                                        <button className="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-sm transition-colors">
                                            Detalhes
                                        </button>
                                    </td>
                                </tr>
                                <tr className="hover:bg-gray-50 transition-colors">
                                    <td className="py-3 px-4 text-blue-600 font-medium">#ORD-2349</td>
                                    <td className="py-3 px-4">Fortaleza, CE</td>
                                    <td className="py-3 px-4">16/07/2024</td>
                                    <td className="py-3 px-4">
                                        <span className="px-2 py-1 bg-gray-100 text-gray-800 rounded-full text-xs">
                                            No prazo
                                        </span>
                                    </td>
                                    <td className="py-3 px-4">
                                        <button className="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-sm transition-colors">
                                            Detalhes
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <div className="flex justify-center mt-6">
                        <nav className="inline-flex rounded-md shadow-sm" aria-label="Pagination">
                            <a
                                href="https://webcrumbs.cloud/placeholder"
                                className="relative inline-flex items-center px-3 py-2 bg-primary-500 text-white font-medium text-sm rounded-l-md hover:bg-primary-600 transition-colors"
                            >
                                1
                            </a>
                            <a
                                href="https://webcrumbs.cloud/placeholder"
                                className="relative inline-flex items-center px-3 py-2 bg-white text-gray-700 border border-gray-300 text-sm font-medium hover:bg-gray-50 transition-colors"
                            >
                                2
                            </a>
                            <a
                                href="https://webcrumbs.cloud/placeholder"
                                className="relative inline-flex items-center px-3 py-2 bg-white text-gray-700 border border-gray-300 text-sm font-medium hover:bg-gray-50 transition-colors"
                            >
                                3
                            </a>
                            <a
                                href="https://webcrumbs.cloud/placeholder"
                                className="relative inline-flex items-center px-3 py-2 bg-white text-gray-700 border border-gray-300 text-sm font-medium rounded-r-md hover:bg-gray-50 transition-colors"
                            >
                                <span className="material-symbols-outlined text-sm">arrow_forward</span>
                            </a>
                        </nav>
                    </div>
                    {/* Next: "Add a filterable search bar above the tables" */}
                </section>
                {/* Next: "Add a map component showing delivery routes" */}
            </div>
        </div>
    );
};

export default Home;