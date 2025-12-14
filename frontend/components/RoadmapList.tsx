"use client";
import React from "react";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { CheckSquare, ListChecks } from "lucide-react";

interface RoadmapListProps {
    roadmap: string[];
}

const RoadmapList: React.FC<RoadmapListProps> = ({ roadmap }) => {
    return (
        <Card className="w-full max-w-4xl bg-gray-900/50 border-gray-700 text-white mt-8">
            <CardHeader>
                <CardTitle className="flex items-center gap-2 text-xl text-green-400">
                    <ListChecks className="h-5 w-5" />
                    Personalized Roadmap
                </CardTitle>
            </CardHeader>
            <CardContent>
                <ul className="space-y-3">
                    {roadmap.map((step, index) => (
                        <li key={index} className="flex items-start gap-3 p-3 rounded-lg bg-gray-800/50 hover:bg-gray-800 transition-colors border border-gray-700/50">
                            <input type="checkbox" className="mt-1 h-5 w-5 rounded border-gray-600 bg-gray-700 text-green-500 focus:ring-green-500 focus:ring-offset-gray-900 accent-green-500 cursor-pointer" />
                            <span className="text-gray-200">{step}</span>
                        </li>
                    ))}
                    {roadmap.length === 0 && <p className="text-gray-400 italic">Excellent repository! No major improvements needed.</p>}
                </ul>
            </CardContent>
        </Card>
    );
};

export default RoadmapList;
