"use client";
import React, { useState } from "react";
import { useRouter } from "next/navigation";
import { Search } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

export default function RepoInput() {
    const [url, setUrl] = useState("");
    const router = useRouter();

    const handleAnalyze = () => {
        if (!url) return;
        router.push(`/result?repo=${encodeURIComponent(url)}`);
    };

    return (
        <div className="flex flex-col sm:flex-row gap-4 w-full max-w-lg mx-auto">
            <Input
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                className="h-12 bg-gray-900 border-gray-700 focus-visible:ring-blue-500 text-white"
                placeholder="https://github.com/username/repository"
            />
            <Button
                onClick={handleAnalyze}
                size="lg"
                className="h-12 px-8 bg-blue-600 hover:bg-blue-700 text-white font-semibold"
            >
                Analyze <Search className="ml-2 h-4 w-4" />
            </Button>
        </div>
    );
}
